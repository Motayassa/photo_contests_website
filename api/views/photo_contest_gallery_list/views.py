from django.shortcuts import render

from models_appl.models.photo.models import Photo


def photo_contest_gallery_list(request):
    photos = Photo.approved.all()
    return render(request, "api/photo/gallery.html", {"photos": photos})
