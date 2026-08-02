from app.services.analyze import analyze_review

def run_test():
    review_text = "The product was great, but the delivery was late."
    analysis_result = analyze_review(review_text)
    print("Analysis Result:", analysis_result)

if __name__ == "__main__":
    run_test()