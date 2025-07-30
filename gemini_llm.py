# gemini_llm.py
import google.generativeai as genai

genai.configure(api_key="AIzaSyAmzjuGVGB95qzrkbeIhcjpPOmlC2-mQzo")  # Replace with your actual key

model = genai.GenerativeModel('gemini-pro')

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
