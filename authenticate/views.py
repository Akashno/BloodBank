from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from authenticate.decorators import unauthenticated_user
from authenticate.forms import CreateHospitalForm, CreateUserForm
from authenticate.models import HospitalProfile, UserProfile


@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_page')
            hprofile = HospitalProfile.objects.filter(hospital=user)
            if hprofile:
                return redirect('hospital')
            else:
                return redirect('user')

        else:
            messages.error(request, 'invalid username or password')
    context = {}
    return render(request, 'authenticate/login_page.html', context)


def logout_page(request):
    logout(request)
    return redirect('index')

@unauthenticated_user
def register_hprofile(request, username=None):
    if request.method == "POST":
        hospital = User.objects.filter(username=username)
        register_number = request.POST.get('register-number')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        district = request.POST.get('district')
        town = request.POST.get('town')
        uniquern = HospitalProfile.objects.filter(register_number=register_number)
        if uniquern:
            messages.error(request, 'Register number already registered')
            return redirect('register_hprofile', username)
        profile = HospitalProfile(
            hospital=hospital[0],
            register_number=register_number,
            phone=phone,
            state=state,
            district=district,
            town=town
        )

        profile.save()
        messages.success(request, 'Registeration successfull for ' + str(username))
        return redirect('login_page')
    context = {}
    return render(request, 'authenticate/register_hprofile.html', context)

@unauthenticated_user
def register_hospital(request):
    form = CreateHospitalForm()
    if request.method == "POST":
        form = CreateHospitalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('register_hprofile', request.POST.get('username'))

    context = {'form': form}
    return render(request, 'authenticate/register_hospital.html', context)

@unauthenticated_user
def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_uprofile', request.POST.get('username'))
    context = {'form': form}
    return render(request, 'authenticate/register_user.html', context)

@unauthenticated_user
def register_uprofile(request, username=None):
    if request.method == "POST":
        user = User.objects.filter(username=username)
        blood = request.POST.get('blood')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        town = request.POST.get('town')
        district = request.POST.get('district')
        state = request.POST.get('state')

        profile = UserProfile(
            user=user[0],
            blood=blood,
            phone=phone,
            address=address,
            town=town,
            district=district,
            state=state,
        )
        profile.save()
        messages.success(request, 'Registeration successfull for ' + str(username))
        return redirect('login_page')
    context = {}
    return render(request, 'authenticate/register_uprofile.html', context)
