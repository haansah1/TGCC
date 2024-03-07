from django.contrib.auth.models import User
from django.db import models

class ImageGroup(models.Model):
    name = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.ForeignKey(ImageGroup, on_delete=models.SET_NULL, null=True, blank=True)
    # name = models.CharField(max_length=100)
    image = models.ImageField(null = True, blank = True);

    # def __str__(self):
    #     return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " " 
        return url
    

# Create your models here.


