import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from authenticate.models import HospitalProfile, UserProfile

from hospital.models import BloodStock, RequestBlood
from user.decorators import user_view
from user.models import BloodRequest
from django.shortcuts import render, redirect

from authenticate.models import HospitalProfile


def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_page')
        hprofile = HospitalProfile.objects.filter(hospital=request.user)
        if hprofile:
            return redirect('hospital')
        else:
            return redirect('user')
    context = {}
    return render(request, 'user/index.html',context)

@login_required(login_url='login_page')
@user_view
def user(request):
    if request.method == "POST":
        patient_name = request.POST.get('patient-name')
        patient_age = request.POST.get('patient-age')
        blood_type = request.POST.get('blood')
        target_date = request.POST.get('target-date')
        blood_units = request.POST.get('blood-units')
        phone = request.POST.get('phone')
        hospital_name = request.POST.get('hospital-name')
        hospital_location = request.POST.get('hospital-location')
        patient_address = request.POST.get('patient-address')
        purpose = request.POST.get('purpose')

        bloodrequest = BloodRequest(
            user=request.user,
            patient_name=patient_name,
            patient_age=patient_age,
            blood_type=blood_type,
            blood_units=blood_units,
            target_date=target_date,
            hospital_name=hospital_name,
            hospital_location=hospital_location,
            patient_address=patient_address,
            purpose=purpose,
            phone=phone,
        )
        bloodrequest.save()
        messages.success(request,
                         'Request Placed successfully,We will notify your request to all donors and Health centers after admin verification')
        return redirect('user_profile')
    date = limit_date()
    context = {'date': date}
    return render(request, 'user/index.html', context)

@login_required(login_url='login_page')
@user_view
def blood_request_delete(request, pk):
    items = BloodRequest.objects.filter(id=pk, user=request.user)
    items.delete()
    messages.info(request, 'request deleted successfully')
    return redirect('user_profile')


@login_required(login_url='login_page')
@user_view
def hospital_list(request):
    list = HospitalProfile.objects.all()
    context = {'list': list}
    return render(request, 'user/hospital_list.html', context)


@login_required(login_url='login_page')
@user_view
def blood_stock_view(request, pk):
    # you dont belong here
    if request.user.is_staff:
        return redirect('admin_page')
    if request.user.is_hospital():
        return redirect('login_page')
    # you dont belong here end
    # hospital = User.objects.get(id=pk)
    stock = BloodStock.objects.filter(hospital=pk)
    if stock:
        stock = stock[0]

    context = {'stock': stock}
    return render(request, 'user/blood_stock_view.html', context)


@login_required(login_url='login_page')
@user_view
def user_profile(request):
    # you dont belong here
    if request.user.is_staff:
        return redirect('admin_page')
    if request.user.is_hospital():
        return redirect('login_page')
    # you dont belong here end
    requests = BloodRequest.objects.filter(user=request.user)
    user = UserProfile.objects.get(user_id=request.user.id)
    context = {'user': user, 'requests': requests}
    return render(request, 'user/user_profile.html', context)


@login_required(login_url='login_page')
@user_view
def blood_requests(request):
    user = UserProfile.objects.get(user=request.user)

    user_blood_requests = BloodRequest.objects.filter(blood_type=user.blood, active=True)
    hospital_blood_requests = RequestBlood.objects.filter(blood=user.blood, active=True)
    context = {'user_blood_requests': user_blood_requests, 'hospital_blood_requests': hospital_blood_requests}
    return render(request, 'user/blood_requests.html', context)


def limit_date():
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    if len(str(month)) > 1:
        pass
    else:
        month = str(month).zfill(2)
    if len(str(day)) > 1:
        pass
    else:
        day = str(day).zfill(2)
    date = str(year) + '-' + str(month) + '-' + str(day)
    return date
