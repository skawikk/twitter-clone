from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import FormView, UpdateView
from users.forms import UsersUserLoginForm, UsersUserSingupForm

# Create your views here.
from users.models import User


class UsersUserLoginView(FormView):
    form_class = UsersUserLoginForm
    template_name = "users/generic_form.html"
    success_url = "/"


class UsersUserSingupView(FormView):
    form_class = UsersUserSingupForm
    template_name = "users/generic_form.html"

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            email=form.cleaned_data["email"],
        )
        login(self.request, user)
        return redirect("/")


class UsersUserModifyView(UpdateView):
    model = User
    form_class = UsersUserSingupForm
    template_name = "users/generic_form.html"
