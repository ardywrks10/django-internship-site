from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login 
from django.urls import reverse_lazy 

from .forms import CustomUserCreationForm 
from .models import UserProfile

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

class SignUpView(FormView):
    template_name = "accounts/signup.html"
    form_class    = CustomUserCreationForm 
    success_url   = reverse_lazy("public:index")

    def form_valid(self, form):
        user = form.save()
        UserProfile.objects.create(user=user)
        login(self.request, user)
        return super().form_valid(form)