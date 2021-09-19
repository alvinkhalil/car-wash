from pages.models import About

def about(request):
    about = About.objects.get()
    
    context = {
        "about":about,
    }
    return context
