from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display        = ("title", "slug", "author_name", "published_at", "created_at")
    list_filter         = ("published_at",)
    search_fields       = ("title", "description", "content", "author_name", "tag")
    prepopulated_fields = {"slug": ("title",)}
    ordering            = ("-published_at",)