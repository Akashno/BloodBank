from django.urls import path
from administrator.views import *
urlpatterns = [
    path('', admin_page, name='admin_page'),
    path('blood_request_verify/<int:pk>', blood_request_verify, name='blood_request_verify'),
    path('blood_request_cancel/<int:pk>', blood_request_cancel, name='blood_request_cancel'),
    path('request_blood_verify/<int:pk>', request_blood_verify, name='request_blood_verify'),
    path('request_blood_cancel/<int:pk>', request_blood_cancel, name='request_blood_cancel'),

]