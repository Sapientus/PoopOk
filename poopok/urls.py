# [poopok]/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('games/', include('games.urls')),
    path('stars/', include('stars.urls')),
    path('health/', include('health.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
