from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BloodRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)
    patient_age = models.IntegerField()
    blood_type = models.CharField(max_length=20)
    blood_units = models.IntegerField(null=True,blank=True)
    target_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField(null=False)
    hospital_name = models.CharField(max_length=100,null=True)
    hospital_location = models.CharField(max_length=100,null=True)
    patient_address = models.TextField(null=True)
    purpose = models.TextField(null=True)
    active = models.BooleanField(default=False)

