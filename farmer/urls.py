
from django.urls import path
from . import views
urlpatterns = [
    path('accounts/login/',views.loginfarmer,name="login"),
    path('logout/',views.farmerLogout,name="logout"),
    path('',views.home,name="Home"),
    path('addfarmer/',views.addFarmer,name="AddFarmer"),
    path('updatefarmer/<id>/',views.updateFarmer,name="UpdateFarmer"),
    path('deletefarmer/<id>/',views.deleteFarmer,name="DeleteFarmer"),
    path('addquestion/',views.addQuestion,name="AddQuestion"),
    path('updatequestion/<id>/',views.updateQuestion,name="UpdateQuestion"),
    path('showQuestion/',views.showQuestion,name="ShowQuestion"),
    path('addAnswer/<q_id>/',views.addAnswer,name="AddAnswer"),
    path('updateAnswer/<id>/',views.updateAnswer,name="UpdateAnswer")
]

