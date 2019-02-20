from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Input email"),
        help_text=_("Enter the same password as before, for verification."),
    )