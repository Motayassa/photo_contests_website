from django.contrib import admin

from models_app.models.comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "photo", "content", "publicate_date", "parrent_comment"]
    list_filter = ["author", "photo", "publicate_date"]
    search_fields = ["author", "content"]
    date_hierarchy = "publicate_date"
    ordering = ["publicate_date", "author"]
