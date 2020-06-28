from django.shortcuts import render
from .models import Project
from blog.models import Blogs


# Create your views here.

def home(request):
    projects = Project.objects.all()
    blogs = Blogs.objects.all()
    return render(request, "portfolio/home.html", {'projects': projects, 'blogs': blogs})


def aboutus(request):
    projects = Project.objects.all()
    return render(request, "portfolio/aboutus.html", {'projects': projects})
