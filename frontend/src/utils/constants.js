// API Endpoints
export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/auth/login',
    SIGNUP: '/auth/signup',
    LOGOUT: '/auth/logout',
    REFRESH: '/auth/refresh',
  },
  BOOKS: {
    GET_ALL: '/books',
    GET_ONE: (id) => `/books/${id}`,
    CREATE: '/books',
    UPDATE: (id) => `/books/${id}`,
    DELETE: (id) => `/books/${id}`,
  },
  WATCHLIST: {
    GET_ALL: '/watchlist',
    ADD: '/watchlist',
    REMOVE: (id) => `/watchlist/${id}`,
  },
  OCR: {
    SCAN: '/ocr/scan',
  },
}

// App Config
export const APP_CONFIG = {
  APP_NAME: 'Shelfcare',
  API_BASE_URL: process.env.VITE_API_BASE_URL || '/api',
  TOKEN_STORAGE_KEY: 'token',
  USER_STORAGE_KEY: 'user',
}

// Messages
export const MESSAGES = {
  SUCCESS: {
    LOGIN: 'Successfully logged in!',
    SIGNUP: 'Account created successfully!',
    LOGOUT: 'Successfully logged out!',
    BOOK_ADDED: 'Book added to your library!',
    BOOK_DELETED: 'Book removed from your library!',
    ADDED_TO_WATCHLIST: 'Added to your watchlist!',
    REMOVED_FROM_WATCHLIST: 'Removed from your watchlist!',
  },
  ERROR: {
    INVALID_EMAIL: 'Please enter a valid email address',
    WEAK_PASSWORD: 'Password must be at least 6 characters',
    PASSWORDS_DONT_MATCH: 'Passwords do not match',
    SOMETHING_WENT_WRONG: 'Something went wrong. Please try again later.',
  },
}
