from django.db import models
from models import photo


class Like(models.Model):
    #  user_id
    photo = models.ForeignKey(
        photo, on_delete=models.CASCADE, related_name="photo_like"
    )
