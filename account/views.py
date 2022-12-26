from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from account.forms import UserCreationForm, UserLoginForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponse('success')
        return HttpResponse('failed')
    return render(request, 'account/login.html', {'form': form})
