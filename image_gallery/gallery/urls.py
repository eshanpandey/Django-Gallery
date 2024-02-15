from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('upload/', views.upload_image, name='upload_image'),
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
