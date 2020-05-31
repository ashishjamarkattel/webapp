from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import profile_text,user_profile

class editprofile(UserChangeForm):

    class Meta:
        model=User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

class profile_home(forms.ModelForm):
    class Meta:
        model = profile_text
        fields = (
            'text',

        )

class user_profile_edit(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = (

            'images',
            'relation',
            'phone_no'
        )