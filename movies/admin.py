# In current directory import the models file
from .models import Movies

from django.contrib import admin

admin.site.register ( Movies )

