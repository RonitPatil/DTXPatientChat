import re

def summarize_conversation(conversation):
    """Summarize the last few messages for context."""
    return "\n".join([f"{msg['sender']}: {msg['message']}" for msg in conversation])

def extract_entities(user_message):
    """Extract key entities from the user message."""
    entities = {}

    # Regex patterns for various entities
    medication_pattern = r'\b(?:taking|prescribed|on)\s+([a-zA-Z\s]+)\b'
    frequency_pattern = r'\b(?:twice|three times|once|daily|weekly|every)\s+(?:a day|day|week)\b'
    appointment_pattern = r'\b(?:appointment|schedule|time|meet|visit)\s*:\s*([a-zA-Z\s,0-9]+)'
    diet_pattern = r'\b(?:diet|eating habits|nutrition|food)\s*:\s*([a-zA-Z\s,]+)'

    # Match medication
    medication_match = re.search(medication_pattern, user_message, re.IGNORECASE)
    if medication_match:
        entities['medication'] = medication_match.group(1).strip()

    # Match frequency
    frequency_match = re.search(frequency_pattern, user_message, re.IGNORECASE)
    if frequency_match:
        entities['frequency'] = frequency_match.group(0).strip()

    # Match appointment details
    appointment_match = re.search(appointment_pattern, user_message, re.IGNORECASE)
    if appointment_match:
        entities['appointment'] = appointment_match.group(1).strip()

    # Match diet details
    diet_match = re.search(diet_pattern, user_message, re.IGNORECASE)
    if diet_match:
        entities['diet'] = diet_match.group(1).strip()

    return entities