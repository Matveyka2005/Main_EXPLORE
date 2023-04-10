from django.forms import ModelForm
from django.http import request
from .models import *
from django import forms


class BbForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["rubric"].empty_label = "Категория не выбрана"
        

    # АВТОМАТИЧЕСКОЕ ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ

    class Meta:
        model = Bb
        fields = ("title", "content", "price", "rubric", "photo")

