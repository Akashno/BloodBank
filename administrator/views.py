from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

# Create your views here.
from authenticate.models import HospitalProfile
from hospital.models import RequestBlood
from user.models import BloodRequest


def admin_page(request):
    # you dont belong here
    if not request.user.is_staff:
        return redirect('login_page')
    # you dont belong here end
    bloodrequests = BloodRequest.objects.filter(active=False)
    requestbloods = RequestBlood.objects.filter(active=False)
    context={'bloodrequests':bloodrequests,'requestbloods':requestbloods}
    return render(request, 'administrator/admin_page.html', context)


def blood_request_verify(request,pk):
    # you dont belong here
    if not request.user.is_staff:
        return redirect('login_page')
    # you dont belong here end
    item = BloodRequest.objects.get(id=pk)
    item.active = True
    item.save()
    messages.success(request, 'User blood request verified')
    return redirect('admin_page')

def blood_request_cancel(request, pk):
    # you dont belong here
    if not request.user.is_staff:
        return redirect('login_page')
    # you dont belong here end
    item = BloodRequest.objects.get(id=pk)
    item.delete()
    messages.success(request, 'User blood request Canceled')
    return redirect('admin_page')

def request_blood_verify(request,pk):
    # you dont belong here
    if not request.user.is_staff:
        return redirect('login_page')
    # you dont belong here end
    item = RequestBlood.objects.get(id=pk)
    item.active = True
    item.save()
    messages.success(request, 'Hospital blood request verified')
    return redirect('admin_page')

def request_blood_cancel(request, pk):
    # you dont belong here
    if not request.user.is_staff:
        return redirect('login_page')
    # you dont belong here end
    item = RequestBlood.objects.get(id=pk)
    item.delete()
    messages.success(request, 'Hospital blood request canceled')
    return redirect('admin_page')

