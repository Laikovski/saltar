from django.contrib import messages
from .forms import CreateUserForm, AddWork
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Work
from .forms import UpdateProfile
from django.contrib.auth.models import User

def RegisterPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'пользователь создан, выполни вход)')
            return redirect('login')
        else:
            messages.info(request, 'что-то пошло не так)')
    context = {'form': form}
    return render(request, 'profiles/register.html', context)

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cabinet')
        else:
            messages.info(request, 'Пароль или логин неверны')
    context = {}
    return render(request, 'profiles/login.html', context)


def UserCabinet(request):
    form = AddWork()
    profile_user = request.user.id
    profile_info = Profile.objects.filter(user_id=profile_user)
    work_info = Work.objects.filter(work_id=profile_user)


    if request.method == 'POST':
        form = AddWork(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'profile': profile_info, 'work': work_info, 'form': form}
    return render(request, 'profiles/cabinet.html', context)

def EditCabinet(request):
    context = {}
    data = Profile.objects.get(user_id= request.user.id)
    context['data']=data

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        car_model = request.POST['car-model']
        car_number = request.POST['car-number']
        vin = request.POST['vin']

        data.name = name
        data.phone = phone
        data.car_model = car_model
        data.car_number = car_number
        data.vin = vin
        data.save()

        return redirect('cabinet')
    return render(request, 'profiles/edit_info.html', context)

def LogoutUser(request):
    logout(request)
    return render(request, 'profiles/login.html')