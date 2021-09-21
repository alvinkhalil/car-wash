from django.contrib import admin
from django.db import models
from reservation.models import ReservationModel
# Register your models here.
class RezervmodelAdmin(admin.ModelAdmin):
    list_display = ["name","phone","status","created_date"]
    list_editable = ["status"]
    list_filter = ["created_date","status"]
    search_fields = ["name","phone","email"]

admin.site.register(ReservationModel,RezervmodelAdmin)
