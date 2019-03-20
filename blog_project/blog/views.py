from django.shortcuts import render

posts = [
  {
    'author': 'CoreyMS',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'March 18,2019'
  },
  {
    'author': 'Joblack',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'March 19,2019'
  },
  {
    'author': 'CoreyMS',
    'title': 'Blog Post 3',
    'content': 'Third post content',
    'date_posted': 'March 20,2019'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')