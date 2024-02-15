# urls.py

from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='gallery/')),  # Redirect root URL to the gallery page
    path('gallery/', include('gallery.urls')),  # Include the URLs from your gallery app
    # Add other URL patterns here as needed
]
