# stars/admin.py
from django.contrib import admin
from .models import Star, Action

admin.site.register(Star)
admin.site.register(Action)
