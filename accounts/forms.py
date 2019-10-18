from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from .models import Student, Profile
from django import forms

from django_summernote.widgets import SummernoteWidget

class SignupForm(UserCreationForm):
    pass
#     class Meta:
        # email = forms.EmailField(
        #     label=_("Input email"),
        #     help_text=_("Enter the same password as before, for verification."),
        # )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'intro': SummernoteWidget(),
        }
