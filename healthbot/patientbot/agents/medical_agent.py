import requests
import os
from dotenv import load_dotenv

load_dotenv()

class MedicalAgent:
    def get_openai_response(self, message, context):
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        system_instructions = f"""
        Patient Details: {context}
        You are an AI trained to assist with general health and lifestyle inquiries, and specific patient health matters.
        Please focus on:
        - General health and lifestyle advice.
        - Details about the patient’s medical condition and medication.
        - Responding to requests for changes in medication and other treatments.
        - If the patient mentions taking unneeded medication, harmful diets, or any behavior that may jeopardize their health, provide a warning about possible risks and suggest safer alternatives.
        Do not engage in or respond to:
        - Any unrelated topics.
        - Sensitive or controversial subjects.
        - Any form of personal advice beyond general health information.
        """
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": system_instructions},
                {"role": "user", "content": message}
            ],
            "max_tokens": 1500
        }
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        if 'choices' in response_data:
            return response_data['choices'][0]['message']['content']
        else:
            error_message = response_data.get('error', {}).get('message', 'Unknown error.')
            print("Error from API:", error_message)
            return f"Error: {error_message}"
