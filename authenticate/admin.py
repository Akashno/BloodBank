
from django.contrib import admin

# Register your models here.
from authenticate.models import HospitalProfile, UserProfile

admin.site.register(HospitalProfile)
admin.site.register(UserProfile)



 # delete requests after target _date
from user.models import BloodRequest
from hospital.models import RequestBlood
import datetime

today = datetime.date.today()
# deleting blood requests of USERS after target date
blood_requests = BloodRequest.objects.all()
for item in blood_requests:
    if today > item.target_date:
        item.delete()

# deleting blood requests of HOSPITALS after target date
request_bloods = RequestBlood.objects.all()
for item in request_bloods:
    if today >item.target_date:
        item.delete()


from django.contrib.auth.models import User

from authenticate.models import HospitalProfile


def is_hospital(self):
    hprofile = HospitalProfile.objects.filter(hospital=self.id)
    if hprofile:
        return True
    else:
        return False

def is_user(self):
    uprofile = UserProfile.objects.filter(user=self.id)
    if uprofile:
        return True
    else:
        return False

User.add_to_class('is_hospital',is_hospital)
User.add_to_class('is_user',is_user)
