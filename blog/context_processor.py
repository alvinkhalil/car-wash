from django.db.models.fields import SlugField
from blog.models import BlogModel, CategoryModel, Comments, ReplyComments
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator


def list(request):
    blogs = BlogModel.objects.filter(status = "active")
    paginator = Paginator(blogs, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "blogs":page_obj,
        "page_obj":page_obj,
    }

    return context