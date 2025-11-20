from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from internship_website import settings

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(f"{name} sent you a message", message, email, [settings.DEFAULT_FROM_EMAIL])
            return render(request, "contact.html", {"form": form, "success": True})
    else:
        raise NotImplementedError("Contact form submission handling is not implemented yet.")
    return render(request, "contact.html", {"form": form})
