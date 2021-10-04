from django.db import models

# Create your models here.


"""
djago model 
html widget 
valdiation
db size
"""

JOB_TYPE  = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Job(models.Model): #table
    title = models.CharField(max_length=100) #colum
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    publishe_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    Category = models.ForeignKey('Category',on_delete=models.CASCADE)


    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self) :
        return self.name

 