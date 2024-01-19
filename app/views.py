from django.shortcuts import render

# Create your views here.

def google(request):
    return render(request,'google.html')

def youtube(request):
    return render(request,'youtube.html')

def instagram(request):
    return render(request,'instagram.html')

def facebook(request):
    return render(request,'facebook.html')