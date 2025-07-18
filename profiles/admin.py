from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'password','latitude','longitude']  # Puedes personalizar columnas a mostrar en la lista
