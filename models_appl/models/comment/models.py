from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from models_appl.models.photo.models import Photo


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_author", null=True
    )
    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE, related_name="photos_comment", null=True
    )
    content = models.TextField(max_length=1000)
    publicate_date = models.DateTimeField(default=timezone.now)
    parrent_comment = models.ForeignKey(
        "self", null=True, blank=True, related_name="comments", on_delete=models.CASCADE
    )
    #  Recursive Model Relationships

    class Meta:
        indexes = [models.Index(fields=["-publicate_date"])]
        ordering = ["-publicate_date"]
        app_label = "api"

    def __str__(self):
        return self.content
