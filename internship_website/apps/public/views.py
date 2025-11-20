from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(LoginRequiredMixin, TemplateView):
    template_name = "about.html"

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

# def about(request: HttpRequest) -> HttpResponse:
#     return render(request, "about.html")
