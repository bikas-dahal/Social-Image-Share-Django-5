from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy

from .models import Post

# Create your views here.

def geneate_blog(request):
    pass


def test(request):
    return render(request, 'blog/index.html')

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_blogs'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_create.html'
    fields = ['title', 'content',  'author']
    
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog_edit.html'
    fields = ['title', 'content', 'author']
    
    
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')