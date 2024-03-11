from django.contrib.auth.models import User
from django.db import models
from models import photo


class Like(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes_author"
    )
    photo = models.ForeignKey(
        photo, on_delete=models.CASCADE, related_name="photo_like"
    )
