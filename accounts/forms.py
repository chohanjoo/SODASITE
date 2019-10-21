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
from accounts.models import User
from django.contrib.auth.forms import (
    AuthenticationForm
)

import logging

from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

logger = logging.getLogger(__name__)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','student_number','password1','password2')

    def save(self, commit=True): # 저장하는 부분 오버라이딩
        user = super(UserCreationForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["email"]
        user.student_number = self.cleaned_data["student_number"]
        if commit:
            user.save()
        return user
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

class LoginForm(AuthenticationForm):


    student_number = forms.CharField(
        label=_("Student Number"),
        strip=False
    )

    def clean(self):
        logger.debug('LoginForm - clean')
        student_id = self.cleaned_data.get('student_number')
        password = self.cleaned_data.get('password')
        logger.debug("%s,%s"%(student_id,password))

        if student_id is not None and password:
            self.user_cache = authenticate(self.request, username=student_id, password=password)
            logger.debug("user_cache : %s" %self.user_cache)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        
        logger.debug("cleaned_data : %s"%self.cleaned_data)

        return self.cleaned_data