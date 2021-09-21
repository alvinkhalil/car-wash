from contact.models import ContactModel
from django.contrib import admin

# Register your models here.
class ContactAdmin(admin.ModelAdmin): 
    list_display = ["name","subject","status","created_date"]
    list_filter = ["name","subject"]
    list_editable = ["status"]
    list_search = ["name","subject"]

admin.site.register(ContactModel,ContactAdmin)