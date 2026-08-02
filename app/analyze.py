import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()



def analyze_review(review_text):
    # create client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key = os.getenv("AZURE_OPENAI_KEY"),
        api_version = "2024-02-01"
    )

    instructions = """
    You are a review analyst. Analyze the following review and return a JSON object with:
    - sentiment: one of "positive", "neutral", or "negative"
    - sentiment_score: a decimal between 0 and 1
    - themes: a list of exactly 3 short theme labels
    Return only the JSON object, nothing else.
    """

    response = client.chat.completions.create(
        model = os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": review_text}
        ]
    )

    return response.choices[0].message.content



