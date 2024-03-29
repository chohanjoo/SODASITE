from django.db import models
from django.urls import reverse
from accounts.models import Profile
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    project_file = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Project, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)