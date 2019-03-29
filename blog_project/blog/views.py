from django.shortcuts import render
from django.views.generic import (ListView,
  DetailView,
  CreateView
)
from .models import Post

def home(request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'blog/home.html', context) #<app>/<model>_<viewtype>.html 

class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  # DESC use -
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  model = Post

class PostCreateView(CreateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})

