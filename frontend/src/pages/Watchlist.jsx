import { useState, useEffect } from 'react'
import { useAuth } from '../hooks/useAuth'

function Watchlist() {
  const [watchlist, setWatchlist] = useState([])
  const [loading, setLoading] = useState(true)
  const { user } = useAuth()

  useEffect(() => {
    // TODO: Fetch watchlist from API
    setLoading(false)
  }, [])

  return (
    <div className="section">
      <div className="container">
        <h2 className="mb-4">Reading Watchlist</h2>
        <p className="text-secondary mb-5">Books you want to read</p>

        {loading ? (
          <div style={{ textAlign: 'center', padding: '3rem', color: '#999' }}>
            <p>Loading your watchlist...</p>
          </div>
        ) : watchlist.length === 0 ? (
          <div style={{ 
            textAlign: 'center', 
            padding: '3rem',
            background: '#f5f5f5',
            borderRadius: '12px'
          }}>
            <p className="text-secondary">Your watchlist is empty. Add books to your reading list!</p>
            <button className="btn btn-primary mt-3" style={{ marginTop: '1rem' }}>
              Browse Books
            </button>
          </div>
        ) : (
          <div>
            {watchlist.map(item => (
              <div 
                key={item.id} 
                className="card mb-3"
                style={{ 
                  borderLeft: '4px solid #000',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  padding: '1.5rem'
                }}
              >
                <div>
                  <h3 style={{ marginBottom: '0.5rem' }}>{item.title}</h3>
                  <p className="text-muted">by {item.author}</p>
                </div>
                <span 
                  style={{
                    background: '#f5f5f5',
                    padding: '0.5rem 1rem',
                    borderRadius: '6px',
                    fontSize: '0.9rem',
                    color: '#666'
                  }}
                >
                  {item.status}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

export default Watchlist
