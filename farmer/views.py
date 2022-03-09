from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout


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