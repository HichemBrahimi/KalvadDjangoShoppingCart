from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

from store.views.forms import RegisterForm
from django.views import View


def Signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("homepage")
    else:
        form = RegisterForm()


    return render(response, "signup.html", {"form": form})
