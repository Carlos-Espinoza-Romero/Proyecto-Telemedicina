from django.db import models
from django.contrib.auth.models import User

class Speciality(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='doctor_profile'
    )
    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.CASCADE,
        related_name='doctors'
    )
    medical_license = models.CharField(
        max_length=100,
        unique=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    day_of_week = models.IntegerField(choices=[
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor} - {self.get_day_of_week_display()} ({self.start_time}-{self.end_time})"


class Patient(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='patient_profile'
    )
    document_number = models.CharField(
        max_length=20,
        unique=True
    )
    address = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('SCHEDULED', 'SCHEDULED'),
        ('COMPLETED', 'COMPLETED'),
        ('CANCELLED', 'CANCELLED'),
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    date_time = models.DateTimeField(db_index=True)
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='SCHEDULED'
    )
    meeting_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient} - {self.date_time}'


class MedicalRecord(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name='medical_record'
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='medical_records'
    )
    diagnosis = models.TextField()
    medical_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Medical Record #{self.id} - {self.patient}'


class Medication(models.Model):
    trade_name = models.CharField(max_length=250)
    generic_name = models.CharField(max_length=250)
    presentation = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trade_name


class Prescription(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )
    prescribed_by = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )
    observations = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Prescription {self.id} - {self.medical_record.patient}'


class PrescriptionDetail(models.Model):
    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name='details'
    )
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE
    )
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration_days = models.PositiveIntegerField()


class ClinicalFile(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name='clinical_file'
    )
    medical_record = models.ForeignKey(
        MedicalRecord,
        on_delete=models.CASCADE,
        related_name='clinical_files'
    )
    url_file = models.URLField()
    file_type = models.CharField(max_length=50)  # PDF, IMAGE, etc.
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'File {self.id} - {self.appointment}'
