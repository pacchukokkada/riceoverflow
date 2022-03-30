
from django.urls import path
from . import views
urlpatterns = [
    path('accounts/login/',views.loginfarmer,name="login"),
    path('logout/',views.farmerLogout,name="logout"),
    path('',views.home,name="Home"),
    path('addfarmer/',views.addFarmer,name="AddFarmer"),
    path('addquestion/',views.addQuestion,name="AddQuestion"),
    path('showQuestion/',views.showQuestion,name="ShowQuestion"),
    path('addAnswer/<q_id>/',views.addAnswer,name="AddAnswer"),
]

