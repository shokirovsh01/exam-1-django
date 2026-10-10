from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100) 
    room = models.CharField(max_length=100) 
    start_date = models.DateField(auto_now=True) 

    def __str__(self):
        return self.name






class Student(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    age = models.PositiveIntegerField() 
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=17)
    grade = models.FloatField()
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

