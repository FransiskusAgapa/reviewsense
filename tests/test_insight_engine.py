from app.services.insight_engine import InsightEngine

def test_insight_engine():
    engine = InsightEngine()
    engine.run()

if __name__ == "__main__":
    print("Running test_insight_engine()...")
    test_insight_engine()
    print("Completed test_insight_engine().")