import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from authenticate.models import HospitalProfile, UserProfile
from hospital.decorators import hospital_view

from hospital.forms import BloodStockForm
from hospital.models import BloodStock, RequestBlood
from user.models import BloodRequest
from user.views import limit_date


@login_required(login_url='login_page')
@hospital_view
def hospital(request):
    context = {}
    return render(request, 'hospital/index.html', context)


@login_required(login_url='login_page')
@hospital_view
def blood_requests_view(request):
    items = BloodRequest.objects.filter(active=True)
    hosrequests = RequestBlood.objects.filter(active=True).exclude(hospital=request.user)
    context = {'items': items, 'hosrequests': hosrequests}
    return render(request, 'hospital/blood_requests_view.html', context)


@login_required(login_url='login_page')
@hospital_view
def hospital_profile(request):
    hospital = HospitalProfile.objects.get(hospital=request.user)
    items = RequestBlood.objects.filter(hospital=request.user)
    context = {'hospital': hospital, 'items': items}
    return render(request, 'hospital/hospital_profile.html', context)


@login_required(login_url='login_page')
@hospital_view
def blood_stock(request):
    stock = BloodStock.objects.filter(hospital=request.user)
    if stock:
        stock = stock[0]
    form = BloodStockForm(initial={'hospital':request.user})
    if request.method == 'POST':
        form = BloodStockForm(data=request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, 'stock added successfullly')
                return redirect('blood_stock')
        else:
            messages.success(request, 'invalid values')
    context = {'form': form, 'stock': stock}
    return render(request, 'hospital/blood_stock.html', context)


@login_required(login_url='login_page')
@hospital_view
def update_blood_stock(request, pk):
    item = BloodStock.objects.get(id=pk)
    item.date_created = datetime.date.today()
    item.save()
    form = BloodStockForm(instance=item)
    if request.method == "POST":
        form = BloodStockForm(data=request.POST, instance=item)
        if form.is_valid():
            form.save()
            item = BloodStock.objects.get(id=pk)
            item.date_created = datetime.datetime.today()
            item.save()
            messages.success(request, 'Stock updated successfully')
            return redirect('blood_stock')

    context = {"form": form}
    return render(request, 'hospital/update_blood_stock.html', context)


@login_required(login_url='login_page')
@hospital_view
def donor_list_view(request):
    donors = UserProfile.objects.all()
    context = {'donors': donors}
    return render(request, 'hospital/donor_list_view.html', context)


@login_required(login_url='login_page')
@hospital_view
def request_blood(request):
    if request.method == "POST":
        hospital = request.user
        blood = request.POST.get('blood')
        target_date = request.POST.get('target-date')
        phone = request.POST.get('phone')
        bloodr = RequestBlood(
            hospital=hospital,
            blood=blood,
            target_date=target_date,
            phone=phone
        )

        bloodr.save()
        messages.success(request,
                         'Blood request placed successfully,We will notify your request to all donors and Health centers after admin verification ')
        return redirect('hospital_profile')
    date = limit_date()
    context = {'date': date}
    return render(request, 'hospital/request_blood.html', context)


@login_required(login_url='login_page')
@hospital_view
def request_blood_delete(request, pk):
    item = RequestBlood.objects.get(id=pk)
    item.delete()
    return redirect('hospital_profile')
