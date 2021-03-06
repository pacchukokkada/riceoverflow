from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import FarmerCreationForm,UserCreationForm,QuestionForm,AnswerForm,FarmerUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Answer, Question,Farmer


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

def updateFarmer(request,id):
    farmer = Farmer.objects.get(id=id)
    user = farmer.user
    if request.method == 'POST':
        user_form = FarmerUpdateForm(request.POST,instance=user)
        farmer_form = FarmerCreationForm(request.POST,instance=farmer)
        if user_form.is_valid() and farmer_form.is_valid():
            user = user_form.save()
            farmer = farmer_form.save(commit=False)
            farmer.user = user
            farmer.save()
            return redirect('Home')
        else:
            print(user_form.errors)
            print(farmer_form.errors)

    user_form = FarmerUpdateForm(instance=user)
    farmer_form =FarmerCreationForm(instance=farmer)
    return render(request,'farmer/addfarmer.html',{
        'u_form':user_form,
        'f_form':farmer_form,
    }
    )

def deleteFarmer(request,id):
    farmer = Farmer.objects.get(id=id)
    if request.user.is_superuser:
        farmer.user.delete()
        return redirect('Home')
    else:
        return HttpResponse("Your not a admin")
    
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
    all_questions = Question.objects.all()
    return render(request,'farmer/home.html',{'questions':all_questions})


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

def updateQuestion(request,id):
    question = Question.objects.get(id=id)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST,instance=question)
        if question_form.is_valid():
            question.save()
            return redirect('Homet')
    question_form = QuestionForm(instance=question)
    return render(request,'farmer/addQuestion.html',{'q_form':question_form})

def showQuestion(request):
    question = Question.objects.all()
    return render(request,'farmer/ex.html',{'questions':question})
@login_required
def addAnswer(request,q_id):
    question=get_object_or_404(Question,id=q_id)
   
    if request.method == 'POST':
        answer = request.POST.get('answer')
        ans = Answer.objects.create(question=question,user=request.user,answer=answer)
        ans.save()
        return redirect('Home')
    return render(request,'farmer/addAnswer.html',)

def updateAnswer(request, id):
    answer = Answer.objects.get(id=id)
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST,instance=answer)
        if answer_form.is_valid():
            answer_form.save()
            return redirect('Home')
    answer_form = AnswerForm(instance=answer)
    return render(request,'farmer/updateAnswer.html',{'answer_form':answer_form})

#deleting questions
def deleteQuestion(request,id):
    question = get_object_or_404(Question,id=id)
    
    question.delete()
    return redirect('Home')

    



