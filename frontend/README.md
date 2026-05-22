# Shelfcare Frontend

A modern React application for book management with features including OCR recognition, watchlist management, and personal book tracking.

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation

```bash
npm install
```

### Development

Start the development server:

```bash
npm run dev
```

The application will be available at `http://localhost:3000`

### Build

Build for production:

```bash
npm run build
```

### Preview Production Build

```bash
npm run preview
```

## 📁 Project Structure

```
src/
├── components/     # Reusable React components
├── pages/         # Page components (Home, BookList, Watchlist)
├── App.jsx        # Main App component with routing
├── main.jsx       # React DOM entry point
└── index.css      # Global styles
```

## 🎨 Styling

This project uses:
- **TailwindCSS** for utility-first CSS
- **Custom CSS** for component-specific styles

## 🔌 API Integration

The frontend is configured to proxy API requests to `http://localhost:8000` (your Python backend).

API calls should use `/api/` prefix:
- `/api/books` → Backend `/books`
- `/api/auth` → Backend `/auth`
- etc.

## 📚 Features

- Home page with feature overview
- Books management
- Reading watchlist
- User authentication (coming soon)
- OCR book recognition (coming soon)

## 🛠️ Technologies

- React 18
- Vite (Build tool)
- React Router v6
- TailwindCSS
- Axios (for API calls)

## 📝 License

See LICENSE in the root directory.
