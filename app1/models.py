from django.db import models

from django.contrib.auth.models import User

from datetime import date

# Create your models here.
class BookManagement(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(default='Available', max_length=50)
    stock = models.IntegerField()
    available_stock = models.IntegerField()
    uid = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    book = models.CharField(max_length=50)
    due = models.DateField(null=True,auto_now=False, auto_now_add=False)
    position = models.CharField(default='not returned', max_length=50)
    status = models.CharField(null=True, max_length=50)
    fine = models.IntegerField(default=0)
    uid = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.book 
    
