
from django.db import models
from django.contrib.auth.models import User

class Farmer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    place = models.CharField(max_length=30)
    taluk = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)
    crops = models.TextField(max_length=40)

    def __str__(self) -> str:
        return self.user.username

class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    views = models.IntegerField(default=0)
    answer = models.IntegerField(default=0)
    date  = models.DateField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.question
    

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question_answers')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.TextField()
    vote = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.question.question

