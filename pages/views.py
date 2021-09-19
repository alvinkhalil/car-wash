from reservation.admin import RezervmodelAdmin
from django.shortcuts import redirect, render
from pages.models import STATUS, About, Clients, Coverimages, Facts, Location, Teams
from reservation.models import ReservationModel
from django.contrib import messages

# Create your views here.

def index(request):
    cover_images = Coverimages.objects.filter(status = "active")
    teams = Teams.objects.all()
    fact = Facts.objects.get(status = "active")
    clients = Clients.objects.filter(status = "active")
    context = {
        "cover_images":cover_images,
        "teams":teams,
        "fact":fact,
        "clients":clients,
    }
    return render(request,"pages/index.html",context)

def about(request):
    teams = Teams.objects.all()
    fact = Facts.objects.get(status = "active")
    context = {
        "teams":teams,
        "fact":fact,
    }
    return render(request, "pages/about.html",context)

def services(request):
    clients = Clients.objects.filter(status = "active")

    context = {
        "clients":clients,
    }

    return render(request,"pages/services.html",context)

def washingpoints(request):
    locations = Location.objects.filter(status = "active")

    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        message = request.POST["message"]

        rezerv = ReservationModel(name = name, phone = phone, email = email, message = message)

        rezerv.save()
        messages.success(request,"Müraciətiniz üçün təşəkkürlər. Sizinlə əlaqə saxlanılacaq")
        return redirect("pages:washingpoints")

    context = {
        "locations":locations,
    }
    return render(request,"pages/washingpoints.html",context)