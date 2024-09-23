from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Patient
from .agents.appointment_agent import AppointmentAgent
from .agents.medical_agent import MedicalAgent
from .utils import summarize_conversation, extract_entities
import datetime

SUMMARY_THRESHOLD=7

def clear_chat(request):
    """Clear the conversation from the session."""
    if 'conversation' in request.session:
        del request.session['conversation']
    if 'appointment_requests' in request.session:
        del request.session['appointment_requests']
    return redirect('http://127.0.0.1:8000/chat') 

def chat_view(request):
    patient = Patient.objects.first()
    patient_context = f"First Name: {patient.first_name}, Last Name: {patient.last_name}, " \
                      f"DOB: {patient.date_of_birth}, Condition: {patient.medical_condition}, " \
                      f"Medication: {patient.medication_regimen}, Next Appointment: {patient.next_appointment}, " \
                      f"Last Appointment: {patient.last_appointment}, Doctor Name: {patient.doctor_name}"

    if 'conversation' not in request.session:
        request.session['conversation'] = []
        
    appointment_agent = AppointmentAgent()
    medical_agent = MedicalAgent()

    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        extracted_entities = extract_entities(user_message)
        print("Extracted Entities:", extracted_entities)

        bot_response = appointment_agent.handle_appointment_request(user_message, patient_context, request)
        if not bot_response:  
            if len(request.session['conversation']) % SUMMARY_THRESHOLD == 0 and len(request.session['conversation']) > 0:
                conversation_summary = summarize_conversation(request.session['conversation'])
                bot_response = medical_agent.get_openai_response(user_message, f"Patient Details: {patient_context}\n{conversation_summary}")
            else:
                bot_response = medical_agent.get_openai_response(user_message, f"Patient Details: {patient_context}")

        request.session['conversation'].append({"sender": "user", "message": user_message, "time": timestamp})
        request.session['conversation'].append({"sender": "bot", "message": bot_response, "time": timestamp})

        request.session.modified = True
        
        return JsonResponse({'bot_message': bot_response})

    context = {
        'patient': patient,
        'conversation': request.session['conversation'],
        'appointment_requests': request.session.get('appointment_requests', [])
    }
    return render(request, 'chat.html', context)
