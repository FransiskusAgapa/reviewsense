import heapq
import json
from collections import Counter
from app.database import get_connection

class InsightEngine():
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def fetch_all_themes(self):
        # Execute SELECT themes FROM review_insights
        self.cur.execute("""
            SELECT themes FROM review_insights
        """)

        # Loop through each row and parse the JSONB array using json.loads()
        rows = self.cur.fetchall()
        all_themes = []
        for row in rows:
            themes_list = row[0] 

            # Build a flat list of all individual themes across all rows
            all_themes.extend(themes_list)

        # Return that flat list
        return all_themes

    def rank_themes(self, themes_list):
        # Count frequency of each theme using Counter(themes_list). This gives you a dictionary like {"battery life": 12, "screen quality": 8, ...}
        counter = Counter(themes_list)

        # Use heapq.nlargest(10, counter.items(), key=lambda x: x[1]) to get the top 10 themes by count
        top_themes = heapq.nlargest(10, counter.items(), key=lambda x: x[1])

        # Return the result
        return top_themes

    def run(self):
        print("Fetching all themes...")
        all_themes = self.fetch_all_themes()
        print("Ranking themes...")
        top_themes = self.rank_themes(all_themes)
        print("Top themes:")
        for theme, count in top_themes:
            print(f"\n- {theme}: {count}")

