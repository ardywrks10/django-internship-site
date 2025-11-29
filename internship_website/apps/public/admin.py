from django.contrib import admin
from .models import BlogPost, Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display        = ("title", "slug", "author_name", "published_at", "created_at")
    list_filter         = ("published_at",)
    search_fields       = ("title", "description", "content", "author_name", "tag")
    prepopulated_fields = {"slug": ("title",)}
    ordering            = ("-published_at",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "short_content", "created_at")
    list_filter = ("created_at", "post")
    search_fields = ("user__username", "content", "post__title")
    autocomplete_fields = ("user", "post")
    ordering = ("-created_at",)

    def short_content(self, obj):
        text = obj.content or ""
        return text[:50] + "..." if len(text) > 50 else text

    short_content.short_description = "Content"