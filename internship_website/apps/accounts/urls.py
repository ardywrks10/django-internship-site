from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomAuthenticationForm  

app_name = "accounts"
urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("login", auth_views.LoginView.as_view(template_name="accounts/login.html", form_class=CustomAuthenticationForm,), name="login",),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
