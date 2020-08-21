from django.urls import path
from ghostpost_app import views

urlpatterns = [
    path('',views.index,name="home_page" ),
    path('sorted/',views.sorted_vote,name="sorted_page" ),
    path('boasts/',views.boasts,name="boasts_page" ),
    path('roasts/',views.roasts,name="roasts_page" ),
    path('upvote/<int:upvote_id>',views.upvote,name="upvote_page" ),
    path('downvote/<int:downvote_id>',views.downvote,name="downvote_page" ),
    path('detailpost/<str:sec_key>',views.detailpost,name="detailpost_page" ),
    path('deletepost/<int:post_id>',views.deletepost,name="deletepost_page" ),
    path('roasts/',views.roasts,name="roasts_page" ),
    path('createPost/',views.createPost,name="createPost_page" ),
]
