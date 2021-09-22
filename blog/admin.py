from blog.models import BlogModel, CategoryModel
from django.contrib import admin
from django.utils.html import format_html


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","created_date"]
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(CategoryModel,CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    def icon(self,object):

        return format_html("<img src = '{}' height = 50 style = 'border-radius: 10px;' ".format(object.image.url))

    list_display = ["title","icon","status","created_date"]
    list_filter = ["created_date","status"]
    list_editable = ["status"]
    search_fields = ["title","text"]
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(BlogModel,BlogAdmin)