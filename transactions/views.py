from rest_framework import generics
from .models import Appointments
from .serializers import AppointmentSerializer
from .nubefact import send_nubefact_invoice
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Transacciones'])
class AppointmentsView(generics.ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        appointment_instance = serializer.save()

        try:
            nubefact_response = send_nubefact_invoice(appointment_instance)
            print(nubefact_response)
            # appointment_instance.invoice_pdf_url = nubefact_response.get('url')
            # appointment_instance.save()
        except Exception as e:
            print(e)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=headers
        )