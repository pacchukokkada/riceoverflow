from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FarmerCreationForm,UserCreationForm
from django.contrib.auth.decorators import login_required



def addFarmer(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        farmer_form = FarmerCreationForm(request.POST)
        if user_form.is_valid() and farmer_form.is_valid():
                user = user_form.save()
                user.save()
                farmer = farmer_form.save(commit=False)
                farmer.user = user
                farmer.save()
                return redirect('Home')
    else:
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
    

def farmerLogout(request):
    user = request.user
    logout(request)
    return redirect('Home')


def home(request):
    return render(request,'farmer/home.html')


@login_required
def addQuestion(request):
    return render(request,'farmer/addQuestion.html') 
