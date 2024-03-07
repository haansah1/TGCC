from django.shortcuts import render
from django.urls import path
from .models import *


def gallery(request):
    image = Gallery.objects.all()
    image_group = ImageGroup.objects.all()
    context = {"images":image, "image_groups":image_group}
    return render(request, "gallery.html", context)


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    
def sermons(request):
    return render(request, "sermons.html")

def testimonies(request):
    return render(request, "testimonies.html")

def giving(request):
    return render(request, "giving.html")

# Create your views here.
