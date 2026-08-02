from unittest.mock import MagicMock, patch
from app.services.insight_engine import InsightEngine

def test_fetch_all_themes_returns_flat_list():
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_conn.cursor.return_value = mock_cur
    mock_cur.fetchall.return_value = [
        (["battery life", "screen quality", "value"],),
        (["battery life", "shipping", "price"],)
    ]

    with patch("app.services.insight_engine.get_connection", return_value=mock_conn):
        engine = InsightEngine()
        result = engine.fetch_all_themes()

        assert "battery life" in result
        assert len(result) == 6

def test_rank_themes_returns_top_themes():
    mock_conn = MagicMock()
    mock_cur = MagicMock()
    mock_conn.cursor.return_value = mock_cur

    with patch("app.services.insight_engine.get_connection", return_value=mock_conn):
        engine = InsightEngine()
        themes = ["quality", "value", "quality", "shipping", "quality"]
        result = engine.rank_themes(themes)

        assert result[0][0] == "quality"
        assert result[0][1] == 3