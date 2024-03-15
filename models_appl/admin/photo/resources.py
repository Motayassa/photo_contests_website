from django.contrib import admin

from models_appl.models.photo.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "photos_image",
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
    search_fields = ["author", "title", "description"]
    date_hierarchy = "add_date"
    ordering = ["add_date", "author"]
