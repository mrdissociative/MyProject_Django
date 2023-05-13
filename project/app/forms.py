
from django import forms
from.models import *

class fileUploadForm(forms.Form):
    username = forms.CharField(max_length=30)
    name = forms.CharField(max_length=30)
    department = forms.CharField(max_length=30)
    phone = forms.IntegerField()
    address = forms.CharField(max_length=100)
    issue = forms.CharField(max_length=100)
    file = forms.FileField()

class RegForm(forms.Form):
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=12)
    department = forms.CharField(max_length=30)
    phone = forms.IntegerField()
    address = forms.CharField(max_length=100)
    email = forms.CharField(max_length=50)

class PasswordChangeForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=12)