from rest_framework import serializers
from django.utils import timezone
from .models import (
    Speciality, Doctor, DoctorSchedule, Patient, 
    Appointment, MedicalRecord, Prescription, 
    PrescriptionDetail, Medication, ClinicalFile
)
from django.contrib.auth.models import User

class UserMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    user_details = UserMinimalSerializer(source='user', read_only=True)
    speciality_name = serializers.ReadOnlyField(source='speciality.name')

    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    user_details = UserMinimalSerializer(source='user', read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Appointment cannot be in the past.")
        return value

    def validate(self, data):
        doctor = data.get('doctor')
        date_time = data.get('date_time')

        if not doctor or not date_time:
            return data

        # Check for double-booking
        # Assuming appointments last 30 minutes for simplicity, or just exact match
        # Let's check for exact overlaps or within a reasonable window
        # For simplicity, we'll check if there's any other appointment at the same time
        # You could also check for a range if duration is known
        if Appointment.objects.filter(doctor=doctor, date_time=date_time, status='SCHEDULED').exists():
            raise serializers.ValidationError("Doctor is already booked at this time.")

        # Validate doctor availability (DoctorSchedule)
        day_of_week = date_time.weekday()
        time = date_time.time()
        
        availability = DoctorSchedule.objects.filter(
            doctor=doctor,
            day_of_week=day_of_week,
            start_time__lte=time,
            end_time__gte=time,
            is_active=True
        ).exists()

        if not availability:
            raise serializers.ValidationError("Doctor is not available at this day/time according to their schedule.")

        return data

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

class PrescriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionDetail
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    details = PrescriptionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Prescription
        fields = '__all__'

class ClinicalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalFile
        fields = '__all__'
