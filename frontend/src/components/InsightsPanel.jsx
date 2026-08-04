import { useState, useEffect } from 'react'
import axios from 'axios'

function InsightsPanel({ productId }) {
    const [insights, setInsights] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        if (!productId) return
        setLoading(true)
        axios.get(`https://reviewsense-api-ve1k.onrender.com/products/${productId}/insights`)
            .then(response => {
                setInsights(response.data)
                setLoading(false)
            })
            .catch(error => {
                console.error('Error:', error)
                setLoading(false)
            })
    }, [productId])

    if (!productId) return <div className="loading">Select a product from the Products tab first.</div>
    if (loading) return <div className="loading">Loading insights...</div>

    return (
        <div>
            <h2 className="section-title">Insights ({insights.length} reviews analyzed)</h2>
            {insights.map(insight => (
                <div key={insight.insight_id} className="review-item">
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
                        <span className={`badge badge-${insight.sentiment_label}`}>
                            {insight.sentiment_label}
                        </span>
                        <span style={{ color: '#8899AA', fontSize: '0.85rem' }}>
                            Score: {(insight.sentiment_score * 100).toFixed(0)}%
                        </span>
                    </div>
                    <div className="themes">
                        {insight.themes.map((theme, i) => (
                            <span key={i} className="theme-tag">{theme}</span>
                        ))}
                    </div>
                </div>
            ))}
        </div>
    )
}


export default InsightsPanel