import {useState, useEffect } from 'react'
import axios from 'axios'

function InsightsPanel({ productId }) {
    const [insights, setInsights] = useState([])

    useEffect(() => {
        axios.get(`http://localhost:8000/products/${productId}/insights`)
            .then(response => setInsights(response.data))
            .catch(error => console.error('Error:', error))
    },[productId])
    

    return (
        <div>
            <h2>Insights for Product ID: {productId}</h2>
            <ul>
                {insights.map(insight => (
                    <li key={insight.insight_id} style={{marginBottom: '8px'}}>
                        Label: <span style={{
                                    backgroundColor: insight.sentiment_label === 'positive' ? 'green' : 
                                                    insight.sentiment_label === 'negative' ? 'red' : 'orange',
                                    color: 'white',
                                    padding: '2px 8px',
                                    borderRadius: '4px'
                                }}>
                                    {insight.sentiment_label}
                                </span><br />
                        Themes: {insight.themes.join(', ')} 
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default InsightsPanel