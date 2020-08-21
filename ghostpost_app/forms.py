
from django.contrib.auth.models import User
from django import forms
from ghostpost_app import models



class BoastsRoastsForm(forms.Form):
    CHOICES = [(True,'boast'),(False,'roast')]
    isboast = forms.ChoiceField(choices=CHOICES)
    post_body = forms.CharField(max_length=280)


