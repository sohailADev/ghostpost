from django.urls import path
from ghostpost_app import views

urlpatterns = [
    path('',views.index,name="home_page" ),
]
