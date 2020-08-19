from django.shortcuts import render,HttpResponseRedirect,reverse
from ghostpost_app import models
from ghostpost_app import forms


# Create your views here.

def index(request):
    
    
    return render(request,'index.htm')