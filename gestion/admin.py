from django.contrib import admin
from .models import Doctor, Patient

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality', 'license_number')
    list_filter = ('speciality',)
    search_fields = ('name',)
    list_per_page = 10

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'social_security_number', 'gender')
    list_filter = ('gender',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)