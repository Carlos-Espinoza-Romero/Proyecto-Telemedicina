from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DoctorViewSet, PatientViewSet, 
    AppointmentViewSet, MedicationViewSet,
    SpecialityViewSet
)

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'specialities', SpecialityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
