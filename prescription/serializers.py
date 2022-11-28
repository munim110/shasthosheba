from rest_framework.serializers import ModelSerializer
from .models import *


class PrescriptionSerializer(ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['doctor', 'patient', 'date', 'description','medicines']

    def create(self, validated_data):
        prescription = Prescription.objects.create(doctor=validated_data['doctor'], patient=validated_data['patient'],
                                                   date=validated_data['date'], description=validated_data['description'])
        medicine_data = validated_data['medicines']
        for medicine in medicine_data:
            medicine = MedicineQuantity.objects.create(medicine=medicine['medicine'], dose=medicine['dose'])
            prescription.medicine.add(medicine)
        return prescription

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
        medicine_data = validated_data.get('medicines', instance.medicines)
        for medicine in medicine_data:
            medicine = MedicineQuantity.objects.create(medicine=medicine['medicine'], dose=medicine['dose'])
            instance.medicine.add(medicine)
        instance.save()
        return instance