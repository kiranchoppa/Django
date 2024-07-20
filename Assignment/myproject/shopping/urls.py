from django.urls import path
from .views import home_page, add_page, delete_item

from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # add for image
from django.conf import settings  # add for image
from django.conf.urls.static import static  # add for image

# app_name = "shopping"

urlpatterns = [
    path("", home_page, name="home_page"),
    path("add_page/", add_page, name="add_page"),
    path("delete-item/<id>/", delete_item, name="delete_item"),
]


# added for image

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
