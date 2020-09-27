from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import tblUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = tblUser
        fields = ('email','password1','password2','Firstname','Lastname','Phone','Gender','Zipcode','date_joined')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = tblUser
        fields = ('email', 'Firstname', 'Lastname', 'Phone', 'Gender', 'Zipcode', 'date_joined')