from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields= ['phone_number', 'first_name', 'last_name', 'age','']                                                                  