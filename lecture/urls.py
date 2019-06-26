from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'lecture'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.add_lecture, name = 'add_lecture'),
    path('<int:pk>/', views.detail_lecture, name = 'detail_lecture'),
    path('<int:pk>/edit/',views.edit_lecture, name = 'edit_lecture'),
    path('<int:pk>/delete/', views.delete_lecture, name = 'delete_lecture'),
]

#서버올릴때 추가하기
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
