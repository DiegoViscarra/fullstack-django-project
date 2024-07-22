from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)
router.register(r'patients', views.PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('appointments/', views.AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', views.AppointmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail'),
    path('medical_histories/', views.MedicalHistoryListCreateView.as_view(), name='medical_history-list-create'),
    path('medical_histories/<int:pk>/', views.MedicalHistoryRetrieveUpdateDestroyView.as_view(), name='medical_history-detail'),
    path('patient_appointments/<int:patient_id>/', views.appointments_patient, name='patient-appointments'),
]