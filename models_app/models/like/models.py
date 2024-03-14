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
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        app_label = "api"
        ordering = ["created_date", "updated_date"]
