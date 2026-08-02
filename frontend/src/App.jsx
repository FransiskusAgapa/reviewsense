import { useState } from 'react'
import ProductList from './components/ProductList'
import ReviewFeed from './components/ReviewFeed'
import InsightsPanel from './components/InsightsPanel'

function App() {
  const [selectedProductId, setSelectedProductId] = useState(null)
  const [view, setView] = useState('products')

  
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>ReviewSense Dashboard</h1>
      
      <nav style={{ marginBottom: '20px' }}>
        <button onClick={() => setView('products')}>Products</button>
        <button onClick={() => setView('reviews')}>Reviews</button>
        <button onClick={() => setView('insights')}>Insights</button>
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
