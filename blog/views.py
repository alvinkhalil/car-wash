from django.db.models.fields import SlugField
from blog.models import BlogModel, CategoryModel
from django.shortcuts import get_object_or_404, render
from taggit.models import Tag

# Create your views here.
def list(request):
    blogs = BlogModel.objects.filter(status = "active")

    context = {
        "blogs":blogs
    }
    return render(request,'blog/bloggrid.html',context)

def postdetail(request,cat_slug, post_slug):
    categories = CategoryModel.objects.all()
    recentpost = BlogModel.objects.order_by("-created_date").filter(status = "active")[:5]
    category = CategoryModel.objects.get(slug = cat_slug)
    post = BlogModel.objects.get(category = category, slug = post_slug)
    tags = Tag.objects.all()


    
    context = {
        "post":post,
        "categories":categories,
        "recentpost":recentpost,
        "tags":tags,

    }
    return render(request,"blog/blogdetail.html",context)

def catposts(request, cat_slug):

    category = CategoryModel.objects.get(slug = cat_slug)
    blogs = BlogModel.objects.filter(category = category)

    context = {
        "blogs":blogs,

    }
    return render(request,"blog/bloggrid.html",context)

def tags(request,tag):

    blogs = BlogModel.objects.filter(tags__name__in =[tag] )
    
    context = {
        "blogs":blogs,

    }
    return render(request,"blog/bloggrid.html",context)

def search(request):

    keyword = request.GET["keyword"]
    if keyword:
        blogs = BlogModel.objects.filter(text__icontains = keyword)

    context = {
        "blogs":blogs,
    }

    return render(request, "blog/bloggrid.html",context)