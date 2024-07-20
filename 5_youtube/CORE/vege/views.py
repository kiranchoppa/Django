from django.shortcuts import render, redirect
from .models import Receipe
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login/")
def receipes(request):

    if request.method == "POST":
        data = request.POST
        name = data.get("receipe_name")
        description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name=name,
            receipe_description=description,
            receipe_image=receipe_image,
        )
        return redirect("/receipes/")

    data = Receipe.objects.all()

    if request.GET.get("search"):
        data = data.filter(receipe_name__icontains=request.GET.get("search"))

    receipe_data = {"receipes": data}

    return render(request, "vege/receipes.html", context=receipe_data)


@login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    os.remove(
        f"/home/bhcp0138/Documents/Django/5_youtube/CORE/public/static/{queryset.receipe_image}"
    )

    queryset.delete()
    return redirect("/receipes/")


@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        queryset.receipe_name = data.get("receipe_name")
        queryset.receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect("/receipes/")

    return render(request, "vege/update_receipes.html", {"receipe": queryset})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid username")
            return redirect("/login/")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/receipes/")

    return render(request, "vege/login.html", {})


@login_required()
def logout_page(request):
    logout(request)
    return redirect("/login/")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user:
            messages.info(request, "User name already taken")
            return redirect("/register/")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")

        # return redirect("/login/")

    return render(request, "vege/register.html", {})
