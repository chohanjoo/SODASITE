from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/',views.MyLoginView.as_view(),name='login'),
    # path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('profile/',views.profile, name='profile'),
    # path('index/', views.index, name="index"),
    path('student/init/',views.inputDatabase),
    path('activate/<str:uidb64>/<str:token>/', views.user_activate, name='activate'),
]
