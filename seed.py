# read the CSV file using Python's built-in csv module
# connect to the database using get_connection() function
# for each row, insert a product first, then insert the review linked to that product

import csv
import os
from app.database import get_connection

with open(os.path.join(os.path.dirname(__file__), 'data', 'reviews.csv'), encoding="utf-8") as f:
    reader = csv.DictReader(f)

    # get the connection and create cursor
    conn = get_connection()
    cur = conn.cursor()

    for row in reader: 
        # inside loop, insert product
        cur.execute(
            """
            INSERT INTO products (asin, name, category)
            VALUES (%s, %s, %s)
            ON CONFLICT (asin) DO NOTHING
""", (row['asins'], row['name'], row['categories'])
        )

        # fetch the product_id back
        cur.execute("SELECT product_id FROM products WHERE asin = %s", (row["asins"],))
        product = cur.fetchone() # fetchone is used to get a single row from the result set
        product_id = product[0] 

        # insert review
        rating = int(row['reviews.rating']) if row['reviews.rating'] else None
        review_date = row['reviews.date'] if row['reviews.date'] else None
        cur.execute(
            """
            INSERT INTO reviews (product_id, reviewer_name, rating, title, body, review_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (product_id, row['reviews.username'], rating, row['reviews.title'], row['reviews.text'], review_date)
        )

    conn.commit()
    cur.close()
    conn.close()
