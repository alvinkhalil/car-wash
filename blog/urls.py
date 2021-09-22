from blog import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('list/',views.list, name="list"),
    path('category/<slug:cat_slug>/<slug:post_slug>',views.postdetail, name="postdetail"),
    path('category/<slug:cat_slug>/',views.catposts,name = "catposts"),
    path('tags=<slug:tag>/',views.tags,name = "tagposts"),
    path('search',views.search,name="search")

]