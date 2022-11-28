from django.db import models
from doctor.models import Doctor
from patient.models import Patient

# Create your models here.

class MedicineQuantity(models.Model):
    medicine = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)

    def __str__(self):
        return self.medicine.name + ' ' + self.dose

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    medicines = models.ManyToManyField(MedicineQuantity)
    description = models.TextField()

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return self.patient.user.username + ' ' + self.doctor.user.username