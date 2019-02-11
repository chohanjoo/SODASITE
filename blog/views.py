from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)

@login_required
def post_new(request):
    pass
