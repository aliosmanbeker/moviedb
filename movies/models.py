from django.db import models

class category(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    film_aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)
