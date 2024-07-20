from django.urls import path
from .views import home

app_name = "manga_ranking"

urlpatterns = [
    path("", home, name="home"),
]
