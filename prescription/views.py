from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from doctor.models import *
from patient.models import *

# Create your views here.

class PrescriptionViewSet(ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        # user = self.request.user
        # doctor = Doctor.objects.get(user=user)
        # if doctor:
        #     return Prescription.objects.filter(doctor=doctor)
        # else:
        #     intermediary = Intermediary.objects.get(user=user)
        #     if intermediary:
        #         patients = Patient.objects.filter(intermediary=intermediary)
        #         return Prescription.objects.filter(patient__in=patients)
        #     else:
        #         return Prescription.objects.all()
        return Prescription.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def get_serializer_context(self):
        return {'request': self.request}