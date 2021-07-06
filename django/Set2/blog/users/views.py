from django.shortcuts import render, get_object_or_404
from .models import Post 
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import  LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
class PostListView(ListView):
    template_name = 'users/home.html'                   #DEFAULT - <app>/<model>_<viewtype>.html
    model = Post
    context_object_name = 'posts'                       #DEFAULT - object_list
    ordering = ['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):                       #DEFAULT - object
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):                       #DEFAULT -  <app>/<model>_form.html   (for createview and updateview)
    model = Post                                        #DEFAULT - form
    fields = ['title', 'description', 'featured_image', 'content']  
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):                       #DEFAULT -  <app>/<model>_form.html   (for createview and updateview)
    model = Post                                        #DEFAULT - form
    fields = ['title', 'description', 'featured_image', 'content']  
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):                       #DEFAULT - object
    model = Post                                                                                 #DEFAULT - <model>_confirm_delete.html
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def like(request):
    if request.method == 'POST':
        postid = int(request.POST.get('postid'))
        post = get_object_or_404(Post, id=postid)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        post.save()

        return JsonResponse({'result': post.likes.count(), })