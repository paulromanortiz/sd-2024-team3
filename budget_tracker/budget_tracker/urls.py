from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth authentication
    path('', include('budget.urls')),  # Main app URLs
]