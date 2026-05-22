import cv2
import pytesseract
import pandas as pd
import numpy as np
import easyocr
import re
import requests

# Load EasyOCR once (IMPORTANT)
reader = easyocr.Reader(['en', 'hi'])


# -------------------------------
# Preprocessing
# -------------------------------
def preprocess_image(file_bytes):
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 3)

    thresh = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    return img, thresh

# -------------------------------
# Region Function
# -------------------------------

def detect_text_regions(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # edge detection
    edged = cv2.Canny(gray, 50, 150)

    # dilation to connect text regions
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilated = cv2.dilate(edged, kernel, iterations=1)

    contours, _ = cv2.findContours(
        dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    regions = []

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # filter noise (important)
        if w > 100 and h > 30:
            regions.append((x, y, w, h))

    return regions

# ------------------------------
# OCR per region
# ------------------------------

def ocr_on_regions(img):
    regions = detect_text_regions(img)

    texts = []
    confidences = []

    for (x, y, w, h) in regions:
        roi = img[y:y+h, x:x+w]

        text, conf = tesseract_ocr(roi)

        if conf < 50:
            text2, conf2 = easyocr_ocr(roi)
            if conf2 > conf:
                text, conf = text2, conf2

        if text.strip():
            texts.append(text)
            confidences.append(conf)

    final_text = " ".join(texts)
    avg_conf = sum(confidences)/len(confidences) if confidences else 0

    return final_text, avg_conf

# -------------------------------
# Tesseract OCR
# -------------------------------
def tesseract_ocr(img):
    import pytesseract
    import pandas as pd

    data = pytesseract.image_to_data(
        img,
        output_type=pytesseract.Output.DATAFRAME
    )

    # -------------------------------
    # FIX: Clean text column safely
    # -------------------------------
    if "text" not in data.columns:
        return "", 0

    # Convert everything to string first
    data["text"] = data["text"].astype(str)

    # Remove NaN-like values
    data = data[data["text"] != "nan"]

    # Strip spaces
    data["text"] = data["text"].str.strip()

    # Remove empty strings
    data = data[data["text"] != ""]

    if data.empty:
        return "", 0

    # -------------------------------
    # Extract text + confidence
    # -------------------------------
    text = " ".join(data["text"].tolist())

    # confidence sometimes has -1 → ignore those
    valid_conf = data[data["conf"] > 0]["conf"]

    confidence = valid_conf.mean() if not valid_conf.empty else 0

    return text, float(confidence)

#-------------------------------
# EasyOCR
# -------------------------------
def easyocr_ocr(img):
    results = reader.readtext(img)

    if not results:
        return "", 0

    text = " ".join([r[1] for r in results])
    confidence = sum([r[2] for r in results]) / len(results)

    return text, confidence


# -------------------------------
# Rotation handling
# -------------------------------
def rotate_image(img, angle):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(img, matrix, (w, h))


def try_rotations(img):
    best_img = img
    best_conf = 0

    for angle in [0, 90, 180, 270]:
        rotated = rotate_image(img, angle)
        _, conf = tesseract_ocr(rotated)

        if conf > best_conf:
            best_conf = conf
            best_img = rotated

    return best_img


# -------------------------------
# OCR Switch Logic
# -------------------------------
def run_ocr(img):
    text, conf = tesseract_ocr(img)

    if conf < 60:
        text2, conf2 = easyocr_ocr(img)

        if conf2 > conf:
            return text2, conf2

    return text, conf


# -------------------------------
# Clean text
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# -------------------------------
# Parse book
# -------------------------------
def parse_book(text):
    lines = text.split()

    if not lines:
        return None, None

    # try meaningful chunks instead of fixed slicing
    title_candidates = []

    for i in range(len(lines)):
        for j in range(i+2, min(i+6, len(lines))):
            phrase = " ".join(lines[i:j])
            if len(phrase) > 5:
                title_candidates.append(phrase)

    title = max(title_candidates, key=len) if title_candidates else None

    # naive author detection
    author = None
    if "dan brown" in text:
        author = "Dan Brown"

    return title, author

# -------------------------------
# Google API Lookup
# -------------------------------
def enrich_book_from_google(query):
    try:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
        res = requests.get(url, timeout=5).json()

        if "items" not in res:
            return None

        book = res["items"][0]["volumeInfo"]

        return {
            "title": book.get("title"),
            "author": book.get("authors", [None])[0],
            "publishedDate": book.get("publishedDate"),
            "description": book.get("description"),
            "thumbnail": book.get("imageLinks", {}).get("thumbnail")
        }

    except Exception:
        return None


# -------------------------------
# MAIN PIPELINE
# -------------------------------
def process_book_image(file_bytes):
    original_img, processed_img = preprocess_image(file_bytes)

    processed_img = try_rotations(processed_img)

#   text, conf = run_ocr(processed_img)
    text, conf = ocr_on_regions(original_img)

    cleaned = clean_text(text)

    title, author = parse_book(cleaned)
    query = cleaned
    enriched = enrich_book_from_google(query)

    if enriched:
        return {
            "title": enriched["title"],
            "author": enriched["author"],
            "confidence": conf,
            "source": "google_books"
        }

    return {
        "title": title,
        "author": author,
        "confidence": conf,
        "source": "ocr"
    }
