from io import BytesIO

from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.urls import reverse
from django.utils import timezone
from PIL import Image, ImageOps

from .managers import (
    ApprovedManager,
    DeletedManager,
    ModerationManager,
    RejectedManager,
)


class Photo(models.Model):

    class Status(models.TextChoices):
        APPROVED = "App", "Approved"
        REJECTED = "Rej", "Rejected"
        DELETED = "Del", "Deleted"
        MODERATION = "Mod", "Moderation"

    # Managers_list
    objects = models.Manager()
    approved = ApprovedManager()
    rejected = RejectedManager()
    deleted = DeletedManager()
    moderation = ModerationManager()

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="authors_photos", null=True
    )
    title = models.CharField(max_length=75)
    photos_image = models.ImageField(upload_to="images/%Y/%m/%d/")
    thumbnail300px = models.ImageField(
        upload_to="images_thumbnail/%Y/%m/%d/", null=True, blank=True
    )
    slug = models.SlugField(
        max_length=75, unique_for_date="publicate_date", null=True, blank=True
    )
    description = models.TextField(max_length=1000)
    likes_amount = models.IntegerField(default=0, blank=True)
    comments_amount = models.IntegerField(default=0, blank=True)
    publicate_date = models.DateTimeField(default=timezone.now)
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.MODERATION
    )

    class Meta:
        indexes = [models.Index(fields=["-add_date"])]
        ordering = ["-add_date"]
        app_label = "api"

    def save(self, *args, **kwargs):
        self.thumbnail300px = self.make_thumbnail(self.photos_image)
        super().save(*args, **kwargs)

    def valid_extension(self, _img):
        if ".jpg" in _img:
            return "JPEG"
        elif ".jpeg" or ".JPG" in _img:
            return "JPEG"
        elif ".png" in _img:
            return "PNG"

    def make_thumbnail(self, image):
        im = Image.open(image)
        im = ImageOps.contain(im, (300, 300), method=Image.LANCZOS)
        im = ImageOps.exif_transpose(im)
        im_io = BytesIO()
        im.save(im_io, self.valid_extension(image.name), optimize=False, quality=99)
        thumbnail = File(im_io, name=image.name)
        return thumbnail

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("api:photo_detail", args=[self.id])
