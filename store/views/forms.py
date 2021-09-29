from django import forms
from django.contrib.auth.forms import UserCreationForm
from store.models.customer import Customer


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Customer

        fields = ["username", "email", "password1", "password2"]
