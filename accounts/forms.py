from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomUser

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='username',max_length=50)
    email = forms.EmailField(label='email', max_length=250)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email','password1', 'password2')