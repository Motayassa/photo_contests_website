from io import BytesIO

from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.utils import timezone
from PIL import Image


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
    thumbnail300px = models.ImageField(
        upload_to="images_thumbnail/%Y/%m/%d/", null=True
    )
    description = models.TextField(max_length=1000)
    likes_amount = models.IntegerField(default=0)
    comments_amount = models.IntegerField(default=0)
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
        elif ".jpeg" in _img:
            return "JPEG"
        elif ".png" in _img:
            return "PNG"

    def make_thumbnail(self, image):
        fixed_width = 300
        im = Image.open(image)
        width_percent = fixed_width / float(im.size[0])
        height_size = int(float(im.size[0]) * float(width_percent))
        im = im.resize((fixed_width, height_size), Image.ANTIALIAS)
        im_io = BytesIO()
        im.save(im_io, self.valid_extension(image.name), optimize=True, quality=99)
        thumbnail = File(im_io, name=image.name)
        return thumbnail

    def __str__(self):
        return self.title
