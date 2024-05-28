from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput



class AuthUserForm(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","password")

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"



class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","password")
        widgets = {

            "username": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите имя",
            }),
            "password": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите пароль",
            }),

        }

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


