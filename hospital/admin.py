from django.contrib import admin

# Register your models here.
from hospital.models import BloodStock, RequestBlood


class BloodStockAdmin(admin.ModelAdmin):
    list_display = ('hospital','date_created')

admin.site.register(BloodStock,BloodStockAdmin)
admin.site.register(RequestBlood)
