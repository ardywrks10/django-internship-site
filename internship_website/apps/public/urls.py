from django.urls import path
from .views import index, AboutView, blog_detail

app_name = "public"
urlpatterns = [
    path("", index, name="index"),
    path("about", AboutView.as_view(), name="about"),
    path("blog/<slug:slug>/", blog_detail, name="blog_detail"),
]

