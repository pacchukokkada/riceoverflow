from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import FarmerCreationForm,UserCreationForm,QuestionForm,AnswerForm
from django.contrib.auth.decorators import login_required
from .models import Answer, Question


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
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('Home')
    question_form = QuestionForm()
    return render(request,'farmer/addQuestion.html',{
        'q_form': question_form
    }) 


def showQuestion(request):
    question = Question.objects.all()
    return render(request,'farmer/showQuestion.html',{'questions':question})
@login_required
def addAnswer(request,q_id):
    instance=get_object_or_404(Question,id=q_id)
   
    if request.method == 'POST':
        answer = request.POST.get('answer')
        ans = Answer.objects.create(question=instance,user=request.user,answer=answer)
        ans.save()
        return redirect('Home')
    answer = AnswerForm()
    return render(request,'farmer/addAnswer.html',{'answer':answer})

def deleteQuestion(request,id):
    question = get_object_or_404(Question,id=id)
    question.delete()
    return redirect('Home')

