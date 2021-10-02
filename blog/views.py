from django.db.models.fields import SlugField
from django.http.response import HttpResponseRedirect
from blog.models import BlogModel, CategoryModel, Comments, ReplyComments,BlogLikes
from django.shortcuts import get_object_or_404, redirect, render
from taggit.models import Tag
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def list(request):
    blogs = BlogModel.objects.filter(status = "active")

    paginator = Paginator(blogs, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "blogs":page_obj,
        "page_obj":page_obj,
    }
    return render(request,'blog/bloggrid.html',context)

def postdetail(request,cat_slug, post_slug):
    categories = CategoryModel.objects.all()
    recentpost = BlogModel.objects.order_by("-created_date").filter(status = "active")[:5]
    likedpost = BlogLikes.objects.order_by("-like").all()[:5]
    category = CategoryModel.objects.get(slug = cat_slug)
    post = BlogModel.objects.get(category = category, slug = post_slug)
    tags = Tag.objects.all()
    comments= Comments.objects.filter(post = post)
    reply = ReplyComments.objects.filter()

    try:
        likes =BlogLikes.objects.get(post = post)
    except:
        likes = 0

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message =request.POST["message"]

        comment = Comments.objects.create(name = name, email = email, message = message, post = post)
        comment.save()
        messages.success(request, "Rəyiniz uğurla əlavə oldundu.")

    context = {
        "post":post,
        "categories":categories,
        "recentpost":recentpost,
        "tags":tags,
        "comments":comments,
        "reply":reply,
        "likes":likes,
        "likedpost":likedpost,

    }
    return render(request,"blog/blogdetail.html",context)

def catposts(request, cat_slug):

    category = CategoryModel.objects.get(slug = cat_slug)
    blogs = BlogModel.objects.filter(category = category)
    paginator = Paginator(blogs, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {

        "blogs":page_obj,

    }
    return render(request,"blog/bloggrid.html",context)

def tags(request,tag):

    blogs = BlogModel.objects.filter(tags__name__in =[tag] )

    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blogs":page_obj,

    }
    return render(request,"blog/bloggrid.html",context)

def search(request):

    keyword = request.GET["keyword"]
    if keyword:
        blogs = BlogModel.objects.filter(text__icontains = keyword)
        paginator = Paginator(blogs, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "blogs":page_obj,
        }

        return render(request, "blog/bloggrid.html",context)

def likes(request,id):
    post = BlogModel.objects.get(id = id)
    try:
        like = BlogLikes.objects.get(post = post)

        like.like += 1
        like.save()
    except:
        newLike = BlogLikes.objects.create(post = post, like = 1)
        newLike.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))