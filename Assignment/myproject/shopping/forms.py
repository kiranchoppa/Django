from django import forms
from .models import Items


class AddItem(forms.ModelForm):
    class Meta:
        model = Items
        fields = "__all__"


class CreateUserDetails(forms.Form):
    name = forms.CharField(max_length=50, label="User Name: ")
    phone_number = forms.IntegerField(label="Pone Number: ")
    place = forms.CharField(widget=forms.Textarea, label="Address: ")
    email = forms.EmailField(max_length=50, label="Email: ")
    password = forms.CharField(widget=forms.PasswordInput, label="Password: ")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password: "
    )


class LogInForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
