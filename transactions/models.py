from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    patient = models.ForeignKey(
        'medical.Patient',
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    doctor = models.ForeignKey(
        'medical.Doctor',
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction {self.id} - Patient: {self.patient.user.username}, Doctor: {self.doctor.user.username}, Amount: {self.amount}'
        