from django.db import models
from django.utils import timezone


class Comment(models.Model):
    #  user_id
    #  photo_id
    content = models.TextField(max_length=1000)
    publicate_date = models.DateTimeField(default=timezone.now)
    parrent_comment = models.ForeignKey(
        "self", null=True, related_name="comment", on_delete=models.CASCADE
    )
    #  Recursive Model Relationships

    class Meta:
        indexes = [models.Index(fields=["-publicate_date"])]
        ordering = ["-publicate_date"]
        app_label = "api"

    def __str__(self):
        return self.content
