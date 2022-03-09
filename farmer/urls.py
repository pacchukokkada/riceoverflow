
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginfarmer,name="login"),
    path('',views.home,name="Home"),
]
