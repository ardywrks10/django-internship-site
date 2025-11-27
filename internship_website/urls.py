from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("internship_website.apps.public.urls")),
    path("contact/", include("internship_website.apps.contact.urls")),
    path("accounts/", include("internship_website.apps.accounts.urls")),
]
