from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Photo(models.Model):
    class Status(models.TextChoices):
        APPROVED = "App", "Approved"
        REJECTED = "Rej", "Rejected"
        DELETED = "Del", "Deleted"
        MODERATION = "Mod", "Moderation"

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="authors_photos", null=True
    )
    title = models.CharField(max_length=50)
    photos_image = models.ImageField(upload_to="images/%Y/%m/%d/")
    photos_image200px = models.ImageField(upload_to="images/%Y/%m/%d/")
    #  photos_image200px необходимо подцмать над размером и тем, как редачить фото
    # нужен ли оригинальный url фотографии?
    url = models.URLField()
    description = models.TextField(max_length=1000)
    likes_amount = models.IntegerField()
    commemts_amount = models.IntegerField()
    publicate_date = models.DateTimeField(default=timezone.now)
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.MODERATION
    )

    class Meta:
        indexes = [models.Index(fields=["-add_date"])]
        ordering = ["-add_date"]
        app_label = "api"

    def __str__(self):
        return self.title
