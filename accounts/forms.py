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
        user = super(SignupForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
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

class LoginForm(forms.Form):


    student_number = forms.CharField(
        label=_("Student Number"),
        strip=False
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "username" field.
        # self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        # self.fields['username'].max_length = self.username_field.max_length or 254
        # if self.fields['username'].label is None:
        #     self.fields['username'].label = capfirst(self.username_field.verbose_name)


    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.
        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.
        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.student_number_field.verbose_name},
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
