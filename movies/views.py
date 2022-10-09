from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies

# retrive data from the database
def movies ( request ) :
    data = Movies.objects.all( )
    return render ( request, 'movies/movies.html', { "movies" : data } )


def home ( request ) :
    return HttpResponse ( "Home page" )

# def movies  ( request ) :
#     # template render take three arrguments ( argument, 'template path', <data> )
#     return render ( request, 'movies/movies.html', data )

def detail ( request, id ) :
    data = Movies.objects.get( pk=id )
    return render ( request, 'movies/detail.html', { "movie": data } )