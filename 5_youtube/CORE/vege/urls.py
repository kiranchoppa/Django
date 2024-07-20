from django.urls import path
from .views import (
    receipes,
    delete_receipe,
    update_receipe,
    login_page,
    register_page,
    logout_page,
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # add for image
from django.conf import settings  # add for image
from django.conf.urls.static import static  # add for image

urlpatterns = [
    path("receipes/", receipes, name="receipes"),
    path("delete-receipe/<id>/", delete_receipe, name="delete_receipe"),
    path("update-receipe/<id>/", update_receipe, name="update_receipe"),
    path("login/", login_page, name="login_page"),
    path("register/", register_page, name="register_page"),
    path("logout/", logout_page, name="logout_page"),
]

# add the following for image

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# till this poin
