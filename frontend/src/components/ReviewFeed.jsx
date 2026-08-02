import {useState, useEffect } from 'react'
import axios from 'axios'

function ReviewFeed({ productId }) {
    const [reviews, setReviews] = useState([])

    useEffect(() => {
        axios.get(`http://localhost:8000/products/${productId}/reviews`)
            .then(response => setReviews(response.data))
            .catch(error => console.error('Error:', error))
    }, [productId])

    return (
        <div>
            <h2>Reviews for Product ID: {productId}</h2>
            <ul>
                {reviews.map(review => (
                    <li key={review.review_id} style={{marginBottom: '8px'}}>
                        Review: {review.reviewer_name}<br />
                        Rating: {review.rating}<br />
                        Title: {review.title}<br />
                        Sentiment badge : Coming Soon
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default ReviewFeed