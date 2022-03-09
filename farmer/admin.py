from atexit import register
from operator import imod
from django.contrib import admin
from .models import Farmer
admin.site.register(Farmer)

