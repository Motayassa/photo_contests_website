from django.urls import path

from api.views.photo_contest_gallery_list.views import photo_contest_gallery_list
from api.views.photo_detail.views import photo_detail

app_name = "api"

urlpatterns = [
    path("", photo_contest_gallery_list, name="gallery"),
    path("<int:id>/", photo_detail, name="photo_detail"),
]
