from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Userprofile

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['address', 'zip_code', 'gender', 'account_type']
