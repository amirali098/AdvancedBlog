from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name="blog"

urlpatterns = [    
    path('',views.indexView.as_view(),name="index"),
    path('redirect-with-url/',RedirectView.as_view(url="https://www.google.com"),name="24"),
    path('redirect-with-app-address/',RedirectView.as_view(pattern_name="blog:24"),name="redirect-google"),
    path('post/',views.PostListView.as_view(),name="post_list"),
    path('post/<int:pk>',views.PostDetailView.as_view(),name="post_detail")
   
]