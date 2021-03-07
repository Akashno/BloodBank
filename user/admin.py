from django.contrib import admin

# Register your models here.
from user.models import BloodRequest

class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('user','patient_name','date_created','target_date','phone')

admin.site.register(BloodRequest,BloodRequestAdmin)