from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import Contact,Blogs,Gallery,About,Education,Experience,Skills


# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method=='POST':
        femail=request.POST.get('email')
        fnum=request.POST.get('num')
        fdesc=request.POST.get('desc')
        fname=request.POST.get('name')
        query=Contact(name=fname,email=femail,phonenumber=fnum,description=fdesc)
        messages.success(request,'Thanks for contacting us. We will get back to you soon.')
        query.save()
        return redirect('/contact')

    return render(request,'contact.html')

def about(request):
    abouts=About.objects.all()
    context={"abouts":abouts}
    return render(request,'about.html',context) 

def blog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'blog.html',context) 

def resume(request):
    educations=Education.objects.all()
    experiences=Experience.objects.all()
    skills=Skills.objects.all()
    context={'educations':educations, 'experiences':experiences,"skills":skills}
    return render(request,'resume.html',context)

def gallery(request):
    images=Gallery.objects.all()
    context={"images":images}
    return render(request,'gallery.html',context)


