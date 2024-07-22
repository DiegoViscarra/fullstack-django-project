from rest_framework import viewsets, generics
from .models import Doctor, Patient, Appointment, MedicalHistory
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, MedicalHistorySerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalHistoryListCreateView(generics.ListCreateAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer

class MedicalHistoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def appointments_patient(request, patient_id):
    try:
        appointments = Appointment.objects.filter(patient_id=patient_id)
        serializer = AppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)