from django.contrib import admin
from .models import (
    Speciality, Doctor, DoctorSchedule, Patient, 
    Appointment, MedicalRecord, Prescription, 
    PrescriptionDetail, Medication, ClinicalFile
)

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'speciality', 'medical_license', 'is_active')

@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'day_of_week', 'start_time', 'end_time', 'is_active')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'document_number', 'is_active')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'date_time', 'status')
    list_filter = ('status', 'date_time')

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'trade_name', 'generic_name', 'category', 'is_active')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'appointment', 'created_at')

admin.site.register(Prescription)
admin.site.register(PrescriptionDetail)
admin.site.register(ClinicalFile)
