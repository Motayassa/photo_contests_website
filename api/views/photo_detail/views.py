from django.shortcuts import get_object_or_404, render

from models_appl.models.photo.models import Photo


def photo_detail(request, year, month, day, photo):
    photo = get_object_or_404(
        Photo,
        status=Photo.Status.APPROVED,
        slug=photo,
        publicate_date__year=year,
        publicate_date__month=month,
        publicate_date__day=day,
    )

    return render(request, "api/photo/photo_detail.html", {"photo": photo})
