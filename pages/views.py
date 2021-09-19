from django.shortcuts import render
from pages.models import STATUS, About, Clients, Coverimages, Facts, Teams
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