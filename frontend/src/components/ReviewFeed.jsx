import { useState, useEffect } from 'react'
import axios from 'axios'

function ReviewFeed({ productId }) {
    const [reviews, setReviews] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        if (!productId) return
        setLoading(true)
        axios.get(`https://reviewsense-api-ve1k.onrender.com/products/${productId}/reviews`)
            .then(response => {
                setReviews(response.data)
                setLoading(false)
            })
            .catch(error => {
                console.error('Error:', error)
                setLoading(false)
            })
    }, [productId])

    if (!productId) return <div className="loading">Select a product from the Products tab first.</div>
    if (loading) return <div className="loading">Loading reviews...</div>

    return (
        <div>
            <h2 className="section-title">Reviews ({reviews.length})</h2>
            {reviews.map(review => (
                <div key={review.review_id} className="review-item">
                    <div className="reviewer">{review.reviewer_name}</div>
                    <div className="rating">
                        {'★'.repeat(review.rating || 0)}{'☆'.repeat(5 - (review.rating || 0))}
                        {review.rating ? ` ${review.rating}/5` : ' No rating'}
                    </div>
                    <div className="title">{review.title}</div>
                </div>
            ))}
        </div>
    )
}

export default ReviewFeed