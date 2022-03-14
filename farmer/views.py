from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm,FarmerCreationForm


def addFarmer(request):
    user_form = UserCreationForm()
    farmer_form = FarmerCreationForm()
    return render(request,'farmer/addfarmer.html',
    {
        'u_form':user_form,
        'f_form':farmer_form
    
    })



def loginfarmer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('Home')
        else:
            return HttpResponse("User not found")

    return render(request,'farmer/login.html')
    

def home(request):
    return render(request,'farmer/home.html')