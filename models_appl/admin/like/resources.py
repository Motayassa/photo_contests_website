from django.contrib import admin

from models_appl.models.like.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["author", "photo", "created_date", "updated_date"]
    list_filter = ["created_date", "updated_date", "author", "photo"]
    search_fields = ["created_date", "updated_date", "author", "photo"]
    ordering = ["created_date", "updated_date", "author", "photo"]
