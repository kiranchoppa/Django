from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    people = [
        {"name": "kiran", "age": 14},
        {"name": "Kishore", "age": 22},
        {"name": "Prudhvi", "age": 24},
        {"name": "Lakshman", "age": 23},
    ]

    vegetables = [
        "Pumpkin",
        "Tomato",
        "Potatoe",
    ]

    return render(
        request,
        "home/index.html",
        {"peoples": people, "vegetables": vegetables, "page": "Home"},
    )


def about(request):
    context = {"page": "About"}
    return render(request, "home/about.html", context)


def contact(request):
    context = {"page": "Contact"}
    return render(request, "home/contact.html", context)
