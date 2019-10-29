from django.contrib import admin
from .models import Profile,Student,User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','intro']
# Register your models here.

@admin.register(Student)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','email']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'student_number', 'email', 'is_active']