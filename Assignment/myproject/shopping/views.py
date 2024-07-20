from django.shortcuts import render, redirect
from .models import Items
from . import forms
import os

# Create your views here.


def home_page(request):
    items = Items.objects.all()
    return render(request, "shopping/home.html", {"items": items})


def add_page(request):
    if request.method == "POST":
        form = forms.AddItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("shopping:home_page")
    else:
        form = forms.AddItem()
    return render(request, "shopping/add_page.html", {"form": form})


def delete_item(request, id):
    item = Items.objects.get(id=id)
    os.remove(
        f"/home/bhcp0138/Documents/Django/Assignment/myproject/public/static/{item.image}"
    )
    item.delete()
    return redirect("/")


def update_item(request, id):
    item = Items.objects.get(id=id)

    return render(request, "shopping/update_item.html", {"item": item})
