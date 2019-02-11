from django.urls import path, include
from . import views

app_name= 'blog'

urlpatterns = [
    path('',views.index, name='index'),
    # path('home/', views.index),
    path('<int:pk>/',views.post_detail, name='post_detail'),
]
