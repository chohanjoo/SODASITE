from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
# from django.utils.html import strip_tags

# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from .tokens import account_activation_token
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, primary_key=True)
    photo = models.ImageField(blank=True)
    intro = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk':self.user.primary_key})

class Student(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20) 
    number = models.CharField(max_length=8)
    email = models.EmailField()


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete =models.CASCADE,primary_key=True)
#     photo = models.ImageField(blank=True)
#     bio = models.TextField(blank=True)
#     website_url = models.URLField(blank=True)
    
#     def __str__(self):
#         return self.user.username

#     def get_absolute_url(self):
#         return reverse('profile', kwargs={'pk': self.user.pk})

def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)
        

post_save.connect(on_post_save_for_user,sender=settings.AUTH_USER_MODEL)

# class Student(models.Model):
#     name = models.CharField(max_length=20)
#     studentNumber = models.CharField(max_length=8)
#     email = models.EmailField()

from django.db import models  
from django.core.mail import send_mail  
from django.contrib.auth.models import PermissionsMixin  
from django.contrib.auth.base_user import AbstractBaseUser  
from django.utils.translation import ugettext_lazy as _

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):  
    email = models.EmailField(_('email address'))
    username = models.CharField(_('name'), max_length=30)
    student_number = models.CharField(_('student_number'),max_length=8,unique=True)
    # last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'student_number'
    REQUIRED_FIELDS = ['username','email']

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s' % (self.username)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)