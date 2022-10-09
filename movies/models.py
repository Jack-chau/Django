from unittest.util import _MAX_LENGTH
from django.db import models

class Movies ( models.Model ) :
    title = models.CharField( max_length = 200 )
    year = models.IntegerField()
    
    def __str__ ( self, ) :
        return f'{self.title} from {self.year}'
    
    # def __str__ ( self ) :
    #     return ( ( "%s from %s" ) % ( self.title, self.year ) )