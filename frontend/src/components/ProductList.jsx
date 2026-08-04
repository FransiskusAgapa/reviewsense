import { useState, useEffect } from 'react'
import axios from 'axios'

function ProductList({ onSelectProduct}){
    const [products, setProducts] = useState([])

    useEffect(()=>{
        axios.get('https://reviewsense-api-ve1k.onrender.com')
            .then(response => setProducts(response.data))
            .catch(error => console.error('Error:', error))
    }, []) 

    return (
        <div>
            <h2>Product List</h2>
            <ul>
                {products.map(product =>(
                    <li
                        key={product.product_id}
                        onClick={() => onSelectProduct(product.product_id)}
                        style={{cursor: 'pointer', marginBottom: '8px'}}>
                            Product : {product.name}
                    </li>
                ))}
            </ul>
        </div>
    )
}
    
export default App