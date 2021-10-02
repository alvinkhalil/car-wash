from reservation.forms import PriceForm
from reservation.admin import RezervmodelAdmin
from django.shortcuts import redirect, render
from pages.models import STATUS, About, Clients, Coverimages, Facts, Location, Price, Teams
from reservation.models import ReservationModel
from django.contrib import messages
from blog.models import BlogModel

# Create your views here.

def index(request):
    cover_images = Coverimages.objects.filter(status = "active")
    teams = Teams.objects.all()
    fact = Facts.objects.get(status = "active")
    clients = Clients.objects.filter(status = "active")
    recentpost = BlogModel.objects.order_by("-created_date").filter(status = "active")[:5]
    context = {
        "cover_images":cover_images,
        "teams":teams,
        "fact":fact,
        "clients":clients,
        "recentpost":recentpost,
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
    
    form = PriceForm(request.POST or None)
    if form.is_valid():
        form.save()
        
        messages.success(request,"Müraciətiniz üçün təşəkkürlər. Sizinlə əlaqə saxlanılacaq")



    context = {
        "locations":locations,
        'form':form,
    }
    return render(request,"pages/washingpoints.html",context)

def price(request):
    prices = Price.objects.filter(status = "active")

    context = {
        "prices":prices,
    }
    return render(request, "pages/price.html",context)

def teammate(request):
    teams = Teams.objects.all()

    context = {
        "teams":teams,
    }
    return render(request,"pages/teammate.html",context)