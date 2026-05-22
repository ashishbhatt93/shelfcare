from fastapi import APIRouter, UploadFile, File
from app.ocr.service import process_book_image

router = APIRouter(prefix="/ocr", tags=["OCR"])


@router.post("/scan")
async def scan_book(file: UploadFile = File(...)):
    contents = await file.read()

    result = process_book_image(contents)

    return result
