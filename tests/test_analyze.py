from unittest.mock import MagicMock, patch
from app.services.analyze import analyze_review

def test_analyze_review_returns_json():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = '{"sentiment": "positive", "sentiment_score": 0.9, "themes": ["quality", "value", "shipping"]}'

    with patch("app.services.analyze.AzureOpenAI") as mock_client_class:
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client
        mock_client.chat.completions.create.return_value = mock_response

        result = analyze_review("Great product, fast shipping!")

        assert "sentiment" in result
        assert "themes" in result