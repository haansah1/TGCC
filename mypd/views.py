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
    teams = Teams.objects.all()
    context = {"teams": teams}
    return render(request, "about.html", context)
    
def sermons(request):
    audio = Audios.objects.all()
    context = {"audios":audio,}
    return render(request, "sermons.html", context)

def testimonies(request):
    testimonies = Testimonials.objects.all()
    context = {"testimonies": testimonies}
    return render(request, "testimonies.html", context)

def giving(request):
    return render(request, "giving.html")

# Create your views here.
