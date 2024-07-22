from django.urls import path
from .views import (
    home_page,
    add_page,
    delete_item,
    update_item,
    SignUp_page,
    login_page,
    logout_page,
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # add for image
from django.conf import settings  # add for image
from django.conf.urls.static import static  # add for image

app_name = "shopping"

urlpatterns = [
    path("", home_page, name="home_page"),
    path("add_page/", add_page, name="add_page"),
    path("delete-item/<id>/", delete_item, name="delete_item"),
    path("update-item/<id>/", update_item, name="update_item"),
    path("signup/", SignUp_page, name="signup_page"),
    path("login/", login_page, name="login_page"),
    path("logout/", logout_page, name="logout_page"),
]


# added for image

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
