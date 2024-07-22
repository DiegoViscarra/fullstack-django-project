from datetime import date
from django.core.exceptions import ValidationError

def validate_appointment_date(value):
    if value < date.today():
        raise ValidationError('The date of the appointment cannot be in the past.', params={'value': value})

def validate_social_security_number(value):
    if len(value) != 15 or not value.isdigit():
        raise ValidationError('The social security number must be exactly 15 digits long and contain only digits.', params={'value': value})