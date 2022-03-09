from pyexpat import model
from tkinter import CASCADE
import django
from django.db import models
from django.contrib.auth.models import User
class Farmer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address= models.TextField(max_length=50)

    def __str__(self) -> str:
        return self.user.first_name
