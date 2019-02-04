<<<<<<< HEAD
from django.urls import path,reverse_lazy
from . import views
=======
from django.urls import path, include
>>>>>>> auth_test
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
<<<<<<< HEAD
   path('signup/', views.signup, name='signup'),
   path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('profile/', views.profile, name="profile"),
   path('password_change/', views.MyPasswordChangeView.as_view(),name='password_change'),
#    path('password_change/done/',
#         auth_views.PasswordChangeDoneView.as_view(
#             template_name = 'accounts/password_change_done.html'
#         ), name='password_change_done'),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
=======
    path('signup', views.signup, name="signup"),
    path('login/',views.MyLoginView.as_view(),name='login'),
    # path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('profile/',views.profile, name='profile'),
    # path('index/', views.index, name="index"),
]
>>>>>>> auth_test
