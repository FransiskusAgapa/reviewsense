# Unit tests for analyze_review function
# AzureOpenAI client is mocked to avoid real API calls during CI
from unittest.mock import MagicMock, patch
from app.services.analyze import analyze_review

def test_analyze_review_returns_json():
    # Arrange: mock the entire chat completions create method
    mock_response = MagicMock()
    mock_response.choices[0].message.content = '{"sentiment": "positive", "sentiment_score": 0.9, "themes": ["quality", "value", "shipping"]}'

    with patch("app.services.analyze.AzureOpenAI") as mock_azure:
        mock_instance = mock_azure.return_value
        mock_instance.chat.completions.create.return_value = mock_response

        # Act
        result = analyze_review("Great product, fast shipping!")

        # Assert
        assert "sentiment" in result
        assert "themes" in result