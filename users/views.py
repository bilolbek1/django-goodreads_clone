from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm




class RegisterView(View):
    def get(self, request):
        form_name = RegisterForm()
        context = {
            'form_name': form_name
        }
        return render(request, 'register.html', context)

    def post(self, request):
        form_name = RegisterForm(data=request.POST)
        if form_name.is_valid():
            form_name.save()
            return redirect('login')
        else:
            context = {
                'form_name': form_name
            }
            return render(request, 'register.html', context)


class LoginView(View):
    def get(self, request):
        form_name = AuthenticationForm()
        context = {
            'form_name': form_name
        }
        return render(request, 'login.html', context)

    def post(self, request):
        form_name = AuthenticationForm(data=request.POST)

        if form_name.is_valid():
            user = form_name.get_user()
            login(request, user)

            messages.success(request, 'You have succesfully logged in')
            return redirect('landing')
        else:
            context = {
                'form_name': form_name
            }
            return render(request, 'login.html', context)















































