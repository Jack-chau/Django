from django.http import HttpResponse
from django.shortcuts import render

# we can save data as globle variable
data = {
    "movies" : [
        {
            'id' : 5,
            'title' : 'Jaws',
            'years' : 1669,
        },
        {
            'id' : 6,
            'title' : 'Sharknado',
            'years' : 1600,
        },
        {
            'id' : 7,
            'title' : 'The Mag',
            'years' : 2000,
        },
    ]
}

def home ( request ) :
    return HttpResponse ( "Home page" )

def movies  ( request ) :
    # template render take three arrguments ( argument, 'template path', <data> )
    return render ( request, 'movies/movies.html', data )

