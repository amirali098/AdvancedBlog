from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView
# Create your views here.

class indexView(TemplateView):
    template_name = "index.html"

    
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model =Post


