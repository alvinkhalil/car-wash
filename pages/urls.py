
from django.urls import path
from pages import views
from contact.views import contact
app_name = "pages"

urlpatterns = [
    path('',views.index,name="index"), 
    path('index/',views.index,name="index"), 
    path('about/',views.about,name = "about"),
    path('services/',views.services,name = "services"),
    path('washingpoints/',views.washingpoints,name = 'washingpoints'),
    path('price/',views.price,name = 'price'),
    path('contact/',contact,name="contact"),
    path('teammates/',views.teammate, name="teammates"),


]