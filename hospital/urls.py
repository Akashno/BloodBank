from django.urls import path

from hospital.views import *

urlpatterns = [
    path('',hospital, name='hospital'),
    path('blood_stock/', blood_stock, name='blood_stock'),
    path('update_blood_stock/<str:pk>',update_blood_stock, name='update_blood_stock'),
    path('hospital_profile/', hospital_profile, name='hospital_profile'),
    path('blood_requests_view/', blood_requests_view, name='blood_requests_view'),
    path('donor_list_view/', donor_list_view, name='donor_list_view'),
    path('request_blood/',request_blood, name='request_blood'),
    path('request_blood_delete/<int:pk>', request_blood_delete, name='request_blood_delete')
]