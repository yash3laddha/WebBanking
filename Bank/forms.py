from django.core import validators
from django import forms
from django.forms import widgets
from .models import *


class updation(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['Acc_Reciever', 'Amt_Transfer']
      