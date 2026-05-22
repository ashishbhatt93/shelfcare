import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'
import { ProtectedRoute } from './components/common/ProtectedRoute'
import Navbar from './components/common/Navbar/Navbar'
import Login from './components/auth/Login/Login'
import Signup from './components/auth/Signup/Signup'
import Home from './pages/Home'
import BookList from './pages/BookList'
import Watchlist from './pages/Watchlist'
import './App.css'

function AppContent() {
  return (
    <Routes>
      {/* Auth Routes */}
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />

      {/* Protected Routes */}
      <Route
        path="/"
        element={
          <ProtectedRoute>
            <>
              <Navbar />
              <main className="container">
                <Home />
              </main>
            </>
          </ProtectedRoute>
        }
      />
      <Route
        path="/books"
        element={
          <ProtectedRoute>
            <>
              <Navbar />
              <main className="container">
                <BookList />
              </main>
            </>
          </ProtectedRoute>
        }
      />
      <Route
        path="/watchlist"
        element={
          <ProtectedRoute>
            <>
              <Navbar />
              <main className="container">
                <Watchlist />
              </main>
            </>
          </ProtectedRoute>
        }
      />

      {/* Catch all - redirect to login */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}

function App() {
  return (
    <Router>
      <AuthProvider>
        <AppContent />
      </AuthProvider>
    </Router>
  )
}

export default App
