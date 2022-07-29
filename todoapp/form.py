from django.forms import forms, ModelForm
from .models import *


class ItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', ]
