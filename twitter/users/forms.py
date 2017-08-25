from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from users.models import User


class UsersUserLoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data["login"]
        passwd = cleaned_data["password"]
        self.user = authenticate(username=login, password=passwd)
        if self.user is None:
            raise ValidationError("Błędny login lub hasło")
        return cleaned_data


class UsersUserSingupForm(forms.ModelForm):
    username = forms.CharField(max_length=64)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
        ]

    def clean_login(self):
        login = self.cleaned_data["username"]
        if User.objects.filter(username=login).exists():
            raise forms.ValidationError("Taki użytkownik istnieje!!")
        return login

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data["password1"]
        pass2 = cleaned_data["password2"]
        if not pass1 == pass2:
            raise ValidationError("Hasła nie są identyczne!")
        return cleaned_data

