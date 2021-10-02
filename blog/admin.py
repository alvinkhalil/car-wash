from blog.views import search
from blog.models import BlogModel, CategoryModel, Comments, ReplyComments
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

class CommentAdmin(admin.ModelAdmin):
    list_display = ["name","email","post","created_date"]
    search_fields = ["name","message"]
    list_filter = ["created_date"]

admin.site.register(Comments, CommentAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ["name","email","created_date"]
    search_fields = ["name","message"]
    list_filter = ["created_date"]

admin.site.register(ReplyComments, ReplyAdmin)
