import { Link } from 'react-router-dom'
import './Navbar.css'

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          📚 Shelfcare
        </Link>
        <ul className="navbar-menu">
          <li className="navbar-item">
            <Link to="/" className="navbar-link">Home</Link>
          </li>
          <li className="navbar-item">
            <Link to="/books" className="navbar-link">Books</Link>
          </li>
          <li className="navbar-item">
            <Link to="/watchlist" className="navbar-link">Watchlist</Link>
          </li>
        </ul>
      </div>
    </nav>
  )
}

export default Navbar
