from blog import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('list/',views.list, name="list")

]