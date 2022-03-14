from atexit import register
from operator import imod
from django.contrib import admin
from .models import Farmer,Question,Answer

admin.site.register(Farmer)
admin.site.register(Question)
admin.site.register(Answer)



