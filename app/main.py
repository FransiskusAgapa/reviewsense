from fastapi import FastAPI, Request, HTTPException
from app.database import get_connection
from fastapi.middleware.cors import CORSMiddleware
from app.rate_limiter import RateLimiter

app = FastAPI(title="ReviewSense", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://reviewsense-frontend-ia6s.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

limiter_rate = RateLimiter(max_tokens=5, refill_rate=1)  # 5 requests per second

@app.get("/")
def root():
    return {"message": "ReviewSense API is running!"}

@app.get("/health")
def health():
    conn = get_connection()
    conn.close()
    return {"database":"connected"}

# get all products
@app.get("/products")
def get_all_products(request: Request):
    if not limiter_rate.is_allowed(request.client.host):
        raise HTTPException(status_code=429, detail="Sorry, Too many requests. Please try again later.")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM products""")
    columns = [desc[0] for desc in cur.description]
    results = [dict(zip(columns, row)) for row in cur.fetchall()]
    conn.close()
    return results

# get product reviews
@app.get("/products/{product_id}/reviews")
def get_product_reviews(product_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM reviews WHERE product_id = %s
        """, (product_id,)
    )
    columns = [desc[0] for desc in cur.description]
    results = [dict(zip(columns, row)) for row in cur.fetchall()]
    conn.close()
    return results

# get product insights
@app.get("/products/{product_id}/insights")
def get_product_insights(product_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT r.*, ri.* FROM review_insights ri
        JOIN reviews r ON ri.review_id = r.review_id
        WHERE r.product_id = %s
        """, (product_id,)
    )
    columns = [desc[0] for desc in cur.description]
    results = [dict(zip(columns, row)) for row in cur.fetchall()]
    conn.close()
    return results











