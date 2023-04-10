from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from users.forms import *
from board.service import *
from board.models import *


'''Регистрация пользователя'''
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register_user.html"
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = get_all_objects(Rubric)
        return context


class LoginUser(AccessMixin, LoginView):
    authentication_form = AuthenticationForm
    template_name = "users/login_user.html"
    redirect_authenticated_user = reverse_lazy("main")

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = get_all_objects(Rubric)
        return context


'''Выход из аккаунта'''
def logout_user(request):
    logout(request)
    return redirect("main")


'''Представление профиля пользователя'''
class UserProfile(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("main")
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['rubrics'] = Rubric.objects.all()
        return data 
        
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
def user_products(request):
    user_products = UserProfileUploads.objects.filter(user=request.user)
    rubrics = Rubric.objects.all()
    data = {
        "user": request.user,
        "rubrics": rubrics,
        "user_products": user_products,
    }
    
    return render(request, "users/user_products.html", context=data)

class UserPasswordChange(PasswordChangeView):
    template_name = "users/pas_ch.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


'''Сброс пароля'''
class AUserPasswordChange(UserPasswordChange):
    template_name = "users/pas_ch.html"
    success_url = reverse_lazy("password_done")
    form_class = PasswordChangeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def password_change_done(request):
    return render(request, "password_change_done.html")

