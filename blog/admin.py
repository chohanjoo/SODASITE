from django.contrib import admin
from .models import Post,Project
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_display_links = ['title']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'writer']
    list_display_links = ['title']