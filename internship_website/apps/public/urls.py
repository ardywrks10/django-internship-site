from django.urls import path
from .views import index, AboutView

app_name = "public"
urlpatterns = [
    path("", index, name="index"),
    path("about", AboutView.as_view(), name="about"),
]
