from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Intermediary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    nid = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    intermediary = models.ForeignKey(Intermediary, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

