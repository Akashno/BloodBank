from django.urls import path

from user.views import *

urlpatterns = [

    path('user/', user, name='user'),
    path('hospital_list', hospital_list, name='hospital_list'),
    path('blood_stock_view/<int:pk>', blood_stock_view, name='blood_stock_view'),

    path('user_profile/', user_profile, name='user_profile'),
    path('blood_request_delete/<int:pk>', blood_request_delete, name='blood_request_delete'),
    path('blood_requests/', blood_requests, name='blood_requests'),
]