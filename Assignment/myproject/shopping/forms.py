from django import forms
from .models import Items


class AddItem(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["name", "image", "price", "discount", "size", "discription"]
