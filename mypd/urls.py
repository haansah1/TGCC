from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('sermons', views.sermons, name = 'sermons'),
    path('testimonies', views.testimonies, name = 'testimonies'),
    path('giving', views.giving, name = 'giving'),
    path('gallery', views.gallery, name = 'gallery'),
]
