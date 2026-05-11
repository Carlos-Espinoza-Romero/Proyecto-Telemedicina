from rest_framework import serializers
from .models import (
    Customers,
    Appointments
)
from services.serializers import (
    ServiceSerializer,
    BarberSerializer,
)
from authentication.serializers import UserSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Appointments
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['service'] = ServiceSerializer(instance.service).data
        representation['barber'] = BarberSerializer(instance.barber).data
        representation['user'] = UserSerializer(instance.user).data
        return representation

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer_instance, _ = Customers.objects.get_or_create(
            email=customer_data.get('email', None),
            document_number=customer_data.get('document_number', None),
            defaults=customer_data
        )

        appointment_instance = Appointments.objects.create(
            customer=customer_instance,
            **validated_data
        )
        return appointment_instance

