from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from ghostpost_app import models
from ghostpost_app import forms
from django.db.models.functions import Concat
from django.db.models import Sum
from django.urls import reverse_lazy
import string
import random
# Create your views here.

def index(request):
    all_post = models.BoastsRoastsModel.objects.filter().order_by('-date_created')    
    return render(request,'index.htm',{'all_post':all_post})



def sorted_vote(request):
   
    sort_post_by_vote = models.BoastsRoastsModel.objects.all()
    sort_post_by_vote = list(sort_post_by_vote)
    sort_post_by_vote = sorted(sort_post_by_vote ,key=lambda a: a.total,reverse=True)
    return render(request,'sorted.htm',{'sort_post_by_vote':sort_post_by_vote})
 



def boasts(request):
    all_boasts = models.BoastsRoastsModel.objects.filter(isboast=True).order_by('-date_created') 
    return render(request,'boasts.htm',{'all_boasts':all_boasts})



def roasts(request):
    all_roasts = models.BoastsRoastsModel.objects.filter(isboast=False).order_by('-date_created') 
    return render(request,'roasts.htm',{'all_roasts':all_roasts})



def createPost(request):
    if request.method == "POST":
        form = forms.BoastsRoastsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            secret_key = ''.join(random.choices(string.ascii_letters + string.digits,k=6))
            post = models.BoastsRoastsModel.objects.create(isboast = data.get('isboast'),post_body =data.get('post_body'),s_key=secret_key)
            return render(request,'createPost.htm',{'post':post})
    form = forms.BoastsRoastsForm()
    return render(request,'createPost.htm',{'form':form})
 
def upvote(request,upvote_id):
    post = models.BoastsRoastsModel.objects.get(id=upvote_id)
    post.post_upvote = post.post_upvote + 1
    post.save()    
    return redirect('/')
 
def downvote(request,downvote_id):
    post = models.BoastsRoastsModel.objects.get(id=downvote_id)
    post.post_downvote = post.post_downvote - 1
    post.save()
    return redirect('/')


def detailpost(request,sec_key):
    post = models.BoastsRoastsModel.objects.get(s_key=sec_key)   
    return render(request,'detailpost.htm',{'post':post})

def deletepost(request,post_id):
    models.BoastsRoastsModel.objects.filter(id=post_id).delete()
    return redirect('/')