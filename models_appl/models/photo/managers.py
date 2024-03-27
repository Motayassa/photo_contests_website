from django.db import models


class ApprovedManager(models.Manager):

    def get_queryset(self):
        from .models import Photo

        return super().get_queryset().filter(status=Photo.Status.APPROVED)


class RejectedManager(models.Manager):

    def get_queryset(self):
        from .models import Photo

        return super().get_queryset().filter(status=Photo.Status.REJECTED)


class DeletedManager(models.Manager):

    def get_queryset(self):
        from .models import Photo

        return super().get_queryset().filter(status=Photo.Status.DELETED)


class ModerationManager(models.Manager):

    def get_queryset(self):
        from .models import Photo

        return super().get_queryset().filter(status=Photo.Status.MODERATION)
