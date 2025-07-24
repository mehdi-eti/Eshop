from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


from .forms import LoginForm, RegisterForm
from .models import User


def eshop_login(request):

    if request.user.is_authenticated:
        return redirect('/')

    consumerForm = LoginForm(request.POST or None)

    if request.method == "POST":
        if consumerForm.is_valid():
            phone = consumerForm.cleaned_data.get('phone')
            password = consumerForm.cleaned_data.get('password')
            user = authenticate(request, phone=phone, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                consumerForm.add_error(
                    'password', 'کلمه عبور یا شماره موبایل اشتباه است')

    context = {
        'consumerForm': consumerForm,
    }

    return render(request, 'eshop_login.html', context)


def eshop_register(request):

    if request.user.is_authenticated:
        return redirect('/')

    consumerRegister = RegisterForm(request.POST or None)

    if request.method == "POST":
        if consumerRegister.is_valid():
            phone = consumerRegister.cleaned_data.get('phone')
            email = consumerRegister.cleaned_data.get('email')
            password = consumerRegister.cleaned_data.get('password')
            user = User.objects.create_user(
                phone=phone,
                email=email,
                password=password,
            )
            login(request, user)
            return redirect('/')

    context = {
        'consumerRegister': consumerRegister
    }

    return render(request, 'eshop_register.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')
