from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BloodStock(models.Model):
    hospital = models.OneToOneField(User,on_delete=models.CASCADE)
    # whole blood groups
    w_a_positive = models.IntegerField(default=0,null=True)
    w_a_negative = models.IntegerField(default=0,null=True)
    w_b_positive = models.IntegerField(default=0,null=True)
    w_b_negative = models.IntegerField(default=0,null=True)
    w_ab_positive = models.IntegerField(default=0,null=True)
    w_ab_negative = models.IntegerField(default=0,null=True)
    w_o_positive = models.IntegerField(default=0,null=True)
    w_o_negative = models.IntegerField(default=0,null=True)
    # blood component groups
    b_a_positive = models.IntegerField(default=0,null=True)
    b_a_negative = models.IntegerField(default=0,null=True)
    b_b_positive = models.IntegerField(default=0,null=True)
    b_b_negative = models.IntegerField(default=0,null=True)
    b_ab_positive = models.IntegerField(default=0,null=True)
    b_ab_negative = models.IntegerField(default=0,null=True)
    b_o_positive = models.IntegerField(default=0,null=True)
    b_o_negative = models.IntegerField(default=0,null=True)
    # platelets
    RDP = models.IntegerField(default=0,null=True)
    SDP = models.IntegerField(default=0,null=True)
    FFP = models.IntegerField(default=0,null=True)
    CRYO = models.IntegerField(default=0,null=True)

    date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return str(self.hospital.first_name)


class RequestBlood(models.Model):
    hospital = models.ForeignKey(User,on_delete=models.CASCADE)
    blood = models.CharField(max_length=20)
    target_date = models.DateField()
    phone = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    active =models.BooleanField(default=False,null=True)

    def __str__(self):
        return str(self.hospital.first_name + ' needs ' + self.blood)

