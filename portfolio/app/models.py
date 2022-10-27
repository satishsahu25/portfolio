from ast import Return
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name

class Blogs(models.Model):
    title=models.CharField(max_length=100)
    links=models.TextField(default="#")
    description=models.TextField()
    authorname=models.CharField(max_length=20)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    imgtitle=models.CharField(max_length=20)
    img=models.ImageField(upload_to='gallery',blank=True,null=True)
    imgclass=models.CharField(max_length=20)

    def __str__(self):
        return self.imgtitle

class About(models.Model):
    desc=models.TextField()
    img=models.ImageField(upload_to='about',blank=True,null=True)
    title=models.CharField(max_length=20)
    qoute=models.TextField()
    birth=models.CharField(max_length=20)
    website=models.URLField(max_length=50)
    phone=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    age=models.IntegerField()
    degree=models.CharField(max_length=50)
    emailadd=models.CharField(max_length=30)
    status=models.CharField(max_length=15)
    current=models.TextField()

    def __str__(self):
        return self.title

class Education(models.Model):
    title=models.CharField(max_length=50)
    dates=models.CharField(max_length=15)
    location=models.CharField(max_length=50)
    desc=models.TextField()

    def __Str__(self):
        return self.title
        
class Exppoints(models.Model):
    p1=models.CharField(max_length=30)
    p2=models.CharField(max_length=30)
    p3=models.CharField(max_length=30)
    p4=models.CharField(max_length=30)
    p5=models.CharField(max_length=30)

    def __str__(self):
        return self.p1


class Experience(models.Model):
    title=models.CharField(max_length=50)
    dates=models.CharField(max_length=15)
    location=models.CharField(max_length=50)
    desc=models.ForeignKey(Exppoints,on_delete=models.CASCADE)
    
    def __Str__(self):
        return self.title
class Skills(models.Model):
    filter=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    percent=models.CharField(max_length=10)

    def __str__(self):
        return  self.title


 





