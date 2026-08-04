import { useState, useEffect } from 'react'
import axios from 'axios'

function ProductList({ onSelectProduct }) {
    const [products, setProducts] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        axios.get('https://reviewsense-api-ve1k.onrender.com/products')
            .then(response => {
                setProducts(response.data)
                setLoading(false)
            })
            .catch(error => {
                console.error('Error:', error)
                setLoading(false)
            })
    }, [])

    if (loading) return <div className="loading">Loading products...</div>

    return (
        <div>
            <h2 className="section-title">Products ({products.length})</h2>
            {products.map(product => (
                <div
                    key={product.product_id}
                    className="card"
                    onClick={() => onSelectProduct(product.product_id)}>
                    <h3>{product.name}</h3>
                    <p>{product.category}</p>
                </div>
            ))}
        </div>
    )
}

export default ProductList