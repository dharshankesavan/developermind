from django.shortcuts import render, get_object_or_404
from .models import Blogs


# Create your views here.

def all_blogs(request):
    all_blogs = Blogs.objects.all()
    return render(request, "blog/all_blogs.html", {'all_blogs': all_blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
