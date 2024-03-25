from django.contrib import admin

from models_appl.models.photo.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "photos_image",
        "thumbnail300px",
        "description",
        "status",
        "add_date",
        "publicate_date",
        "likes_amount",
        "comments_amount",
    ]
    list_filter = [
        "author",
        "add_date",
        "publicate_date",
        "status",
        "likes_amount",
        "comments_amount",
    ]
    search_fields = ["author__username", "title", "description"]
    date_hierarchy = "add_date"
    ordering = ["add_date", "author"]
