from django.core.management.base import BaseCommand
from patientbot.models import Patient
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Ensures there is at least one default patient in the database.'

    def handle(self, *args, **kwargs):
        if not Patient.objects.exists():
            self.stdout.write(self.style.SUCCESS('No existing patient found. Creating a default patient...'))
            Patient.objects.create(
                first_name="John",
                last_name="Doe",
                date_of_birth="1990-01-01",
                phone_number="1234567890",
                email="john.doe@example.com",
                medical_condition="Type 2 Diabetes",
                medication_regimen="Metformin 500 mg daily",
                last_appointment="2024-09-09",
                next_appointment="2024-09-30",
                doctor_name="Dr. Smith"
            )
            self.stdout.write(self.style.SUCCESS('Default patient created successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('A patient already exists in the database.'))
