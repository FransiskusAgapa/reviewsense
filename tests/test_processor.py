import pytest
from unittest.mock import MagicMock, patch
from app.services import processor
from app.services.processor import ReviewProcessor
from app.services.insight_engine import InsightEngine

# def test_processor():
#     processor = ReviewProcessor()
#     processor.run()

def test_save_insights_parses_json_correctly():
    # Arrange
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_conn.cursor.return_value = mock_cur 

    with patch("app.services.processor.get_connection", return_value=mock_conn):
        processor = ReviewProcessor()

        # Act
        fake_result = '{"sentiment": "positive", "sentiment_score": 0.9, "themes" : ["quality", "value", "shipping"]}'
        processor.save_insights(1, fake_result)

        # Assert
        assert mock_cur.execute.called

def test_rank_themes_returns_correct_order():
    # Arrange : Create an instance with a mocked connection
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_conn.cursor.return_value = mock_cur

    # Call rank_themes() with a fake themes list where one theme appears more than others
    with patch("app.services.insight_engine.get_connection", return_value=mock_conn):
        engine = InsightEngine()

        # Act
        fake_themes = ["quality", "value", "quality", "shipping", "quality"]
        result = engine.rank_themes(fake_themes)

        # Assert that the themes are ranked correctly
        assert result[0][0] == "quality"
        assert result[0][1] == 3  # "quality" appears 3 times

if __name__ == "__main__":
    # print("Running test_processor()...")
    # test_processor()
    # print("Completed test_processor().")

    # Test
    test_save_insights_parses_json_correctly()
