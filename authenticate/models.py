from django.contrib.auth.models import User
from django.db import models


class HospitalProfile(models.Model):
    hospital = models.OneToOneField(User, on_delete=models.CASCADE)
    register_number = models.CharField(max_length=30, unique=True)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    phone = models.IntegerField()
    is_user = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.hospital.first_name)




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood = models.CharField(max_length=10)
    phone = models.IntegerField()
    address = models.TextField()
    town = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30, null=True)
    is_user = models.BooleanField(default=True, null=True)

    def __str__(self):
        return str(self.user.first_name)