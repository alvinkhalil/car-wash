from blog.models import BlogModel
from django.shortcuts import render

# Create your views here.
def list(request):
    blogs = BlogModel.objects.filter(status = "active")

    context = {
        "blogs":blogs
    }
    return render(request,'blog/bloggrid.html',context)