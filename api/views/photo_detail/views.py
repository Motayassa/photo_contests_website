from django.shortcuts import get_object_or_404, render

from models_appl.models.photo.models import Photo


def photo_detail(request, id):
    photo = get_object_or_404(Photo, id=id, status=Photo.Status.APPROVED)

    return render(request, "api/photo/photo_detail.html", {"photo": photo})
