from django.shortcuts import render, redirect
from .models import Items
from .forms import AddItem, CreateUserDetails, LogInForm
import os
from django.forms import formset_factory

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_page(request):
    items = Items.objects.all()
    return render(request, "shopping/home.html", {"items": items})


def add_page(request):
    if request.method == "POST":
        form = AddItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("shopping:home_page")
    else:
        form = AddItem()
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
    if request.method == "POST":
        form = AddItem(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("shopping:home_page")
    else:
        form = AddItem(instance=item)
    return render(request, "shopping/update_item.html", {"form": form, "item": item})


# tried using formset
"""
def SignUp_page(request):
    # Initialize formset factories
    UserDetailsFormSet = formset_factory(CreateUserDetails, extra=1)
    UserEmailFormSet = formset_factory(CreateUserEmail, extra=1)

    if request.method == "POST":
        # Bind formsets with POST data
        details_formset = UserDetailsFormSet(request.POST)
        email_formset = UserEmailFormSet(request.POST)

        if details_formset.is_valid() and email_formset.is_valid():
            name = ""
            phone_number = ""
            place = ""
            email = ""
            password = ""

            for form in details_formset:
                if form.cleaned_data:
                    name = form.cleaned_data.get("name")
                    phone_number = form.cleaned_data.get("phone_number")
                    place = form.cleaned_data.get("place")

                    user = User.objects.filter(username=name)
                    if user:
                        messages.info(request, "Username already taken")
                        return redirect("/signup/")

            for form in email_formset:
                if form.cleaned_data:
                    email = form.cleaned_data.get("email")
                    password = form.cleaned_data.get("password")
                    confirm_password = form.cleaned_data.get("confirm_password")

                    if password != confirm_password:
                        messages.info(
                            request, "Confirm password did not match with the password"
                        )
                        return redirect("/signup/")

            user = User.objects.create(
                username=name,
                phone_number=phone_number,
                place=place,
                email=email,
            )

            user.set_password(password)
            user.save()
            messages.info(request, "Account created successfully")
            return redirect(
                "/success/"
            )  # Redirect to a success page after successful signup

    else:
        # Initialize empty formsets for GET request
        details_formset = UserDetailsFormSet()
        email_formset = UserEmailFormSet()

    return render(
        request,
        "shopping/signup_page.html",
        {"details_formset": details_formset, "email_formset": email_formset},
    )


"""


def SignUp_page(request):
    if request.method == "POST":
        form = CreateUserDetails(request.POST)
        print("taking input")
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data["name"]
            phone_number = form.cleaned_data["phone_number"]
            place = form.cleaned_data["place"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password = form.cleaned_data["password"]

            user = User.objects.filter(username=username)
            if user:
                messages.info(request, "User name already taken")
                return redirect("/signup/")

            user = User.objects.create(
                username=username,
                # phone_number=phone_number,
                # place=place,
                email=email,
            )

            user.set_password(password)
            user.save()
            print("user saved")
            messages.info(request, "Account created successfully")
            return redirect("/")
    else:
        form = CreateUserDetails()

    return render(request, "shopping/signup_page.html", {"form": form})


def login_page(request):
    return render(request, "shopping/login_page.html", {})
