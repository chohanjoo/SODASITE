from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from .models import Student
class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Input email"),
        help_text=_("Enter the same password as before, for verification."),
    )

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         try:
    #             student = Student.objects.get(name=user.username)
    #         except:
    #             student = None
    #         if student:

    #             # send email for new user
    #             subject = ('Welcome To Soda Site! Confirm Your Email')
    #             message = render_to_string('accounts/email_form.html',{
    #                 'username' : student.name,
    #             })

    #             text_content = strip_tags(message)
                
    #             send_to = [student.email]
    #             msg = EmailMultiAlternatives(subject, text_content, 'vjswl132@gmail.com', send_to)
    #             msg.attach_alternative(message,"text/html")
    #             msg.send()

    #     return user