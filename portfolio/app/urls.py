from app import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('resume',views.resume,name="resume"),
    path('gallery',views.gallery,name="gallery")
]
