from django.db import models
from .validators import validate_appointment_date, validate_social_security_number

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.name} ({self.speciality})"

class PatientGender(models.TextChoices):
    MALE = 'm', 'Male'
    FEMALE = 'f', 'Female'
    OTHER = 'o', 'Other'

class Patient(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateTimeField()
    social_security_number = models.CharField(max_length=15, unique=True, validators=[validate_social_security_number])
    gender = models.CharField(max_length=1, choices=PatientGender.choices, default=PatientGender.MALE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField(validators=[validate_appointment_date])
    reason = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient}'s appointment with {self.doctor} on {self.appointment_date}"

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient}'s medical history ({self.registration_date})"