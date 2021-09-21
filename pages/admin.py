from pages.models import About, Clients, Coverimages, Facts, Location, Price, Teams
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

class CoverimagesAdmin(admin.ModelAdmin):
    def icon(self,object):
        return format_html("<img src = {} width = 100 style = 'border-radius : 10px;' />".format(object.image.url))

    list_display = ["name","icon","status","created_date"]
    list_editable = ["status"]
    list_filter = ["created_date"]

admin.site.register(Coverimages,CoverimagesAdmin)

class TeamsAdmin(admin.ModelAdmin):
    def icon(self,object):
        return format_html("<img src = {} width = 40 style = 'border-radius : 50px; />".format(object.image.url))
    
    list_display = ["name","job","icon","created_date"]
    list_filter = ["created_date"]
    search_fields = ["name"]

admin.site.register(Teams, TeamsAdmin)

admin.site.register(Facts)

class ClientsAdmin(admin.ModelAdmin):
    def icon(self,object):
        return format_html("<img src = {} width = 40 style = 'border-radius: 50px;'/> ".format(object.image.url))
    
    list_display = ["name","icon","job","status","created_date"]
    list_editable = ["status"]
    list_filter = ["created_date"]
    search_fields = ["name"]

admin.site.register(Clients,ClientsAdmin)

class AboutAdmin(admin.ModelAdmin):

    list_display = ["title","created_date"]

admin.site.register(About,AboutAdmin)

class LocationAdmin(admin.ModelAdmin):
    
    list_display = ["id","title","status","is_main","created_date"]
    list_display_links = ["title"]
    list_editable = ["status","is_main"]

admin.site.register(Location,LocationAdmin)


admin.site.register(Price)