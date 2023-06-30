from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    
    return render(request,'index.html')

def profile(request):
    text2=request.POST['text2']
    text3=request.POST['text3']
    return render(request,'profile.html' ,{'text2':text2 ,'text3':text3})


