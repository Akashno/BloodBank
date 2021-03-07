from django.urls import path

from authenticate.views import *
urlpatterns = [
    # registration for hospitals
    path('register_hospital/', register_hospital, name='register_hospital'),
    path('register_hprofile/<str:username>', register_hprofile, name='register_hprofile'),
    # registration for users
    path('register_user/', register_user, name='register_user'),
    path('register_uprofile/<str:username>', register_uprofile, name='register_uprofile'),
    #login and logout for everyone
    path('login_page/', login_page, name='login_page'),
    path('logout_page/',logout_page, name='logout_page'),
]