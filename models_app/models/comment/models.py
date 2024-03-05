from django.db import models
from django.utils import timezone


class comment(models.Model):
    #  user_id
    #  photo_id
    content = models.TextField(max_length=1000)
    publicate_date = models.DateTimeField(default=timezone.now)
    #  необходимо добавить recoursive relationship

    class Meta:
        indexes = [models.Index(fields=["-publicate_date"])]
        ordering = ["-publicate_date"]

    def __str__(self):
        return self.title
