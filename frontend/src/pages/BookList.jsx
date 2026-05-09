import { useState, useEffect } from 'react'
import { useAuth } from '../hooks/useAuth'

function BookList() {
  const [books, setBooks] = useState([])
  const [loading, setLoading] = useState(true)
  const { user } = useAuth()

  useEffect(() => {
    // TODO: Fetch books from API
    setLoading(false)
  }, [])

  return (
    <div className="section">
      <div className="container">
        <h2 className="mb-4">Your Library</h2>
        <p className="text-secondary mb-5">Manage and organize all your books</p>

        {loading ? (
          <div style={{ textAlign: 'center', padding: '3rem', color: '#999' }}>
            <p>Loading your books...</p>
          </div>
        ) : books.length === 0 ? (
          <div style={{ 
            textAlign: 'center', 
            padding: '3rem',
            background: '#f5f5f5',
            borderRadius: '12px'
          }}>
            <p className="text-secondary">No books yet. Start adding books to your collection!</p>
            <button className="btn btn-primary mt-3" style={{ marginTop: '1rem' }}>
              Add Your First Book
            </button>
          </div>
        ) : (
          <div className="grid grid-4">
            {books.map(book => (
              <div key={book.id} className="card" style={{ cursor: 'pointer', textAlign: 'center' }}>
                <img 
                  src={book.cover_url} 
                  alt={book.title}
                  style={{ width: '100%', height: '200px', objectFit: 'cover', marginBottom: '1rem' }}
                />
                <h3 style={{ fontSize: '1rem', marginBottom: '0.5rem' }}>{book.title}</h3>
                <p className="text-muted" style={{ fontSize: '0.9rem' }}>{book.author}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

export default BookList
