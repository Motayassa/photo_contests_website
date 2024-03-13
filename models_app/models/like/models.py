from django.contrib.auth.models import User
from django.db import models

from models_app.models.photo.models import Photo


class Like(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes_author"
    )
    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE, related_name="photos_like"
    )

    class Meta:
        app_label = "api"
