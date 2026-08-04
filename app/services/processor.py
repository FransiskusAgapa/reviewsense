from app.database import get_connection
from app.services.analyze import analyze_review

import json

class ReviewProcessor:
    def __init__(self):
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def fetch_unprocessed_reviews(self):
        self.cur.execute("""
            SELECT r.review_id, r.body 
            FROM reviews r
            LEFT JOIN review_insights ri ON r.review_id = ri.review_id
            WHERE ri.review_id IS NULL
            LIMIT 50""")
        return self.cur.fetchall()

    def save_insights(self, review_id, result):
        # Parse the JSON string into a Python dictionary using json.loads(result), it looks like : {"sentiment":"positive","sentiment_score":0.95,"themes":["battery life","screen quality","value"]}
        parsed_result = json.loads(result)

        # Extract sentiment, sentiment_score, and themes from the dictionary
        sentiment_label = parsed_result.get("sentiment")
        sentiment_score = parsed_result.get("sentiment_score")
        themes = parsed_result.get("themes")

        # Insert those values into review_insights
        self.cur.execute("""
            INSERT INTO review_insights (review_id, sentiment_label, sentiment_score, themes)
            VALUES (%s, %s, %s, %s)
        """, (review_id, sentiment_label, sentiment_score, json.dumps(themes)))

    def run(self):
        # Call fetch_unprocessed_reviews() and store the results
        results = self.fetch_unprocessed_reviews()

        # Loop through each row (each row has review_id and body)
        for row in results:
            review_id, body = row

            # Call analyze_review(body) on each review
            analysis = analyze_review(body)

            # Call save_insights(review_id, result) with the result
            self.save_insights(review_id, analysis)

        # After the loop, commit the transaction with self.conn.commit()
        self.conn.commit()