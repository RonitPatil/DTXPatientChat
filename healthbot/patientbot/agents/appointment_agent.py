import datetime
import os
import requests
import string
from dotenv import load_dotenv

load_dotenv()

class AppointmentAgent:
    def detect_appointment_request(self, message):
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        system_instructions = """
        You are a medical assistant AI. You must determine if the patient is asking to schedule or change an appointment.
        If the patient's message explicitly mentions scheduling, rescheduling, canceling, or confirming an appointment, respond with a simple "yes". 
        If the patient's message is about any other topic, respond with a simple "no". Only respond with "yes" or "no".
        If the patient's message is asking about his next appointment, respond with a simple "no".
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

    def handle_appointment_request(self, message, patient, request):
        cleaned_answer = self.detect_appointment_request(message)
        if self.clean_answer(cleaned_answer) == "yes":
            firstname, lastname, docname, next_appt = self.extract_patient_and_doctor_info(patient)
            bot_response = f"I will convey your request to {docname}."
            appointment_requests = request.session.get('appointment_requests', [])
            appointment_requests.append({
                'message': f"Patient {firstname} {lastname} is requesting an appointment change from '{next_appt}' to '{message}'",
            })
            request.session['appointment_requests'] = appointment_requests
            print(appointment_requests)
            return bot_response
        return None

    def clean_answer(self, answer):
        return answer.strip().lower().strip(string.punctuation)

    def extract_patient_and_doctor_info(self, input_text):
        first_name_start = input_text.find("First Name:") + len("First Name:")
        first_name_end = input_text.find(",", first_name_start)
        first_name = input_text[first_name_start:first_name_end].strip()
        
        last_name_start = input_text.find("Last Name:") + len("Last Name:")
        last_name_end = input_text.find(",", last_name_start)
        last_name = input_text[last_name_start:last_name_end].strip()

        next_appointment_start = input_text.find("Next Appointment:") + len("Next Appointment:")
        next_appointment_end = input_text.find(",", next_appointment_start)
        next_appointment_str = input_text[next_appointment_start:next_appointment_end].strip()

        doctor_name_start = input_text.find("Doctor Name:") + len("Doctor Name:")
        doctor_name = input_text[doctor_name_start:].strip()  
        
        return first_name, last_name, doctor_name, next_appointment_str
