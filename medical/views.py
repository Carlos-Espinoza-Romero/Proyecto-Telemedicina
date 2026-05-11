from rest_framework import viewsets
from .models import Doctor, Patient, Appointment, Medication, Speciality, DoctorSchedule
from .serializers import (
    DoctorSerializer, PatientSerializer, 
    AppointmentSerializer, MedicationSerializer,
    SpecialitySerializer
)
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Medical'])
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

@extend_schema(tags=['Medical'])
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

@extend_schema(tags=['Medical'])
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

@extend_schema(tags=['Medical'])
class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

@extend_schema(tags=['Medical'])
class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
