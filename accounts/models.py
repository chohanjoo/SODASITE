from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete =models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)
        # try:
        #     student = Student.objects.get(name=user)
        # except:
        #     student = None
        # if student:

        #     # send email for new user
        #     subject = ('Welcome To Soda Site! Confirm Your Email')
        #     message = render_to_string('accounts/account_activate_email.html',{
        #         'user' : student.name,
        #         'domail' : 'localhost:8000',
        #         'uid' : urlsafe_base64_encode(force_bytes(student.pk)).decode('utf-8'),
        #         'token' : account_activation_token.make_token(student)
        #     })

        #     text_content = strip_tags(message)
            
        #     send_to = [student.email]
        #     msg = EmailMultiAlternatives(subject, text_content, 'vjswl132@gmail.com', send_to)
        #     msg.attach_alternative(message,"text/html")
        #     msg.send()
        


post_save.connect(on_post_save_for_user,sender=settings.AUTH_USER_MODEL)

class Student(models.Model):
    name = models.CharField(max_length=20)
    studentNumber = models.CharField(max_length=8)
    email = models.EmailField()