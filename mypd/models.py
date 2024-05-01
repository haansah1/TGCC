from django.contrib.auth.models import User
from django.db import models

class ImageGroup(models.Model):
    name = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.name
    
class AudioGroup(models.Model):
    name = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=100, null=True)
    testimony = models.CharField(max_length=5000, null=True)
    image = models.ImageField(null = True, blank = True);
    description = models.CharField(max_length=100, null= True);

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " " 
        return url

class Teams(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(null = True, blank = True);
    description = models.CharField(max_length=100, null= True);

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " " 
        return url
    
class Audios(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(null = True, blank = True);
    description = models.CharField(max_length=100, null= True);
    audio = models.FileField(null = True, blank = True, upload_to="./audio");
    group = models.ForeignKey(AudioGroup, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " " 
        return url
    
    def audioURL(self):
        try:
            url = self.audio.url
        except:
            url = " " 
        return url


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


