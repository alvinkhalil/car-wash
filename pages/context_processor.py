from pages.models import About, Location

def about(request):
    about = About.objects.get()
    
    context = {
        "about":about,
    }
    return context

def location(request):
    settings = Location.objects.get(is_main =True)

    context = {
        "settings":settings,

    }
    return context