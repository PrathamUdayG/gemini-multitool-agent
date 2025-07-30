# router.py
from tools import get_stock_info
from gemini_llm import ask_gemini

stock_keywords = ["stock", "price", "share", "market", "ticker"]

def chatbot_response(query):
    if any(word in query.lower() for word in stock_keywords):
        stock_result = get_stock_info(query)
        if stock_result:
            return stock_result

    # Fallback to Gemini
    return ask_gemini(query)
