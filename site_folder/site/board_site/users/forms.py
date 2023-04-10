from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50, help_text="Введите новое имя", label="Имя")
    email = forms.EmailField(help_text="Введите новый адрес электронной почты", label="Почта")
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "email")

    # def clean(self):
    #     super().clean()
    #     errors = {}
    #
    #     if not self.cleaned_data["username"]:
    #         errors["username"] = ValidationError("Вы забыли ввести свое имя")
    #
    #     if not self.cleaned_data["email"]:
    #         errors["email"] = ValidationError("Вы забыли ввесьти свой email")


# class UserPasswordResetForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ("email", )
#
#     def clean(self):
#         super().clean()
#         errors = {}
#
#         if self.cleaned_data["email"] !=

