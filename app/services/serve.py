from app.database import get_connection

# get all product
def get_all_products():
    # Get a database connection
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * FROM products
        """
    )
    return cur.fetchall()

# get product that matched given id
def get_product_reviews(product_id):
    # Get a database connection
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM reviews WHERE product_id = %s
        """,
        (product_id,)
    )
    return cur.fetchall()

# get product and its reviews given its id
def get_product_insights(product_id):
    # Get a database connection
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT r.*, ri.* FROM review_insights ri
        JOIN reviews r ON ri.review_id = r.review_id
        WHERE r.product_id = %s
        """,
        (product_id,)
    )
    return cur.fetchall()

# Return the results as a list of dictionaries
