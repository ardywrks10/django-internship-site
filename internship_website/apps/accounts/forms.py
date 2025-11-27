from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "minimal-input",
            "placeholder": "Username",
        })
        self.fields["password"].widget.attrs.update({
            "class": "minimal-input",
            "placeholder": "Password",
        })

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "minimal-input",
            "placeholder": "Username"
        })
        self.fields["email"].required = True
        self.fields["email"].widget.attrs.update({
            "class": "minimal-input",
            "placeholder": "Email"
        })
        self.fields["password1"].widget.attrs.update({
            "class": "minimal-input",
            "placeholder": "Password"
        })
        self.fields["password2"].widget.attrs.update({
            "class": "minimal-input",
            "placeholder": "Confirm Password"
        })
