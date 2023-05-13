from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=12)
    date = models.DateField(null=True)
    gender = models.CharField(max_length=30,null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=50,null=True)
    aadharnumber = models.IntegerField(null=True)
    def __str__(self):
        return self.username

class Department(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=12)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    department = models.CharField(max_length=30,null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.firstname

class Complaint(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    file = models.FileField()
    def __str__(self):
        return self.firstname


class Update(models.Model):
    update = models.CharField(max_length=2000)

class Admin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=12)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    def __str__(self):
        return self.firstname






