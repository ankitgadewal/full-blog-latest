from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render, HttpResponse
from .models import Post, Category, Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.
# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/index.html', {'posts':posts})

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    ordering = ['-date_posted']
    paginate_by = 16

class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user-posts.html'
    # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        print(post)
        context['comments'] = Comment.objects.filter(post_id=post).order_by('-date_posted')
        return context
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/new-post.html'
    fields = ['title', 'content', 'category']
    # success_url = '/' instead of this we created a function in models which redirect a user on the post that he created

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post-update.html'
    fields = ['title', 'content']
    # success_url = '/' instead of this we created a function in models which redirect a user on the post that he created

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView, SuccessMessageMixin):
    model = Post
    template_name = 'blog/post-delete.html'
    success_url = '/'
    success_message = 'Post Deleted!!'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCategory(ListView):
    model = Post
    template_name = 'blog/post_category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

def about(request):
    return render(request, 'blog/about.html')

def search(request):
    query = request.GET['query']
    if len(query) > 50 or len(query)<1:
        posts = []
    else:
        posts = Post.objects.filter(title__icontains=query).union(Post.objects.filter(content__icontains=query))
        length = len(posts)
    return render(request, 'blog/search.html', {'posts': posts, 'query': query, 'length':length})

def PostComment(request):
    if request.method == 'POST':
        content = request.POST['content']
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        Comment(content=content, user_id=request.user, post_id=post).save()
        return redirect(f'/post/{post_id}/')