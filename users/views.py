from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, ProfilUpdateForm




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

            messages.success(request, 'You have successfully logged in')
            return redirect('landing')
        else:
            context = {
                'form_name': form_name
            }
            return render(request, 'login.html', context)



class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'user': request.user
        }
        return render(request, 'profile.html', context)

class LogOutView(LoginRequiredMixin, View):
    def get(self, response):
        logout(response)

        messages.success(response, 'You have successfully logged out')
        return redirect('landing')


class ProfilUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        profile_update = ProfilUpdateForm(instance=request.user)
        context = {
            'profile_update': profile_update
        }
        return render(request, 'profile_update.html', context)

    def post(self, request):
        profile_update = ProfilUpdateForm(instance=request.user,
                                          data=request.POST,
                                          files=request.FILES)

        if profile_update.is_valid():
            profile_update.save()
            messages.warning(request, 'You updated your profile')
            return redirect('profile')

        else:
            context = {
                'profile_update': profile_update
            }
            return render(request, 'profile_update.html', context)












































