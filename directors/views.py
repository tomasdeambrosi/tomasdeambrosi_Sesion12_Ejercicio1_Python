from django.shortcuts import render
from .models import Director, Movie, Genre


def index(requests):
    context = {}
    num_directors = Director.objects.all().count()
    num_movies = Movie.objects.all().count()

    return render(requests,
                  'directors/index.html',
                  context={
                      'num_directors': num_directors,
                      'num_movies': num_movies,
                  }
                  )
