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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, primary_key=True)
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