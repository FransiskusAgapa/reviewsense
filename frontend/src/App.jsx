// ReviewSense Dashboard v1.0
import { useState } from 'react'
import ProductList from './components/ProductList'
import ReviewFeed from './components/ReviewFeed'
import InsightsPanel from './components/InsightsPanel'
import './App.css'

function App() {
  const [selectedProductId, setSelectedProductId] = useState(null)
  const [view, setView] = useState('products')

  return (
    <div className="app-container">
      <header className="app-header">
        <h1><span>Review</span>Sense</h1>
        <p style={{ color: '#8899AA', fontSize: '0.9rem', marginTop: '4px' }}>
          Amazon Review Intelligence Dashboard
        </p>
      </header>

      <nav className="nav-bar">
        <button
          className={`nav-btn ${view === 'products' ? 'active' : ''}`}
          onClick={() => setView('products')}>
          Products
        </button>
        <button
          className={`nav-btn ${view === 'reviews' ? 'active' : ''}`}
          onClick={() => setView('reviews')}>
          Reviews
        </button>
        <button
          className={`nav-btn ${view === 'insights' ? 'active' : ''}`}
          onClick={() => setView('insights')}>
          Insights
        </button>
      </nav>

      {view === 'products' && (
        <ProductList onSelectProduct={(id) => {
          setSelectedProductId(id)
          setView('reviews')
        }} />
      )}
      {view === 'reviews' && <ReviewFeed productId={selectedProductId} />}
      {view === 'insights' && <InsightsPanel productId={selectedProductId} />}
    </div>
  )
}

export default App