from django.http import HttpResponse
from django.shortcuts import render

def home ( request ) :
    return HttpResponse ( "Home page" )

def movies  ( request ) :
    # render ( argument, 'template path', <data> )
    return render ( request, 'movies/movies.html', { 'movies': [ 'movies1', 'movies2' ] } )

