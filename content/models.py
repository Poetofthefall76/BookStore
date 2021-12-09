from django.db import models



class Anime(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/")

class Books(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/")
