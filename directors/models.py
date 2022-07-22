from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)
    birthDate = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title

    objects = models.Manager()


class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre
