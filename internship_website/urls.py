from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Path untuk app: public
    path("", include("internship_website.apps.public.urls")),
    # Path untuk app: accounts dan contact
    path("contact/", include("internship_website.apps.contact.urls")),
    path("accounts/", include("internship_website.apps.accounts.urls")),
]
