from blog.models import Blog, Author, Theme, Comment
from django.http import Http404
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from blog.forms import SignUpForm, BlogForm, CommentForm
from django.urls import reverse

# Create your views here.
def blogs(request):
    themes = Theme.objects.all()
    blogs = Blog.objects.all()
    
    context = {
        'blogs': blogs,
        'themes': themes,
    }

    return render(request, 'blogs.html', context=context)

def blog(request, primaryKey):
    blog = Blog.objects.get(pk=primaryKey)
    comments = Comment.objects.filter(blog=primaryKey)
    form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog_detail.html', context=context)

def author(request, primaryKey):
    author = Author.objects.get(pk=primaryKey)
    blogs = Blog.objects.filter(author__last_name__iexact=author.last_name)

    context = {
        'author': author,
        'blogs': blogs,
    }

    return render(request, 'author_detail.html', context=context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            biography = form.cleaned_data.get('biography')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            new_author = Author.objects.create(user=request.user.id, first_name=first_name, last_name=last_name, biography=biography)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

@login_required(login_url='/accounts/login/')
def myposts(request):
    author_id = request.user.id
    author = Author.objects.get(user=author_id)
    blogs = Blog.objects.filter(author__user__id__icontains=author_id)
    context = {
        'author': author,
        'blogs': blogs,
    }
    return render(request, 'author_detail.html', context=context)

@login_required(login_url='/accounts/login/')
def newpost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_title = form.cleaned_data.get('blog_title')
            blog_summary = form.cleaned_data.get('blog_summary')
            blog_text = form.cleaned_data.get('blog_text')
            blog_theme = form.cleaned_data.get('blog_theme')
            author = Author.objects.get(user=request.user.id)
            new_blog = Blog.objects.create(blog_title=blog_title,blog_summary=blog_summary,blog_text=blog_text,blog_theme=blog_theme,author=author)
            return redirect('/')
    else:
        form = BlogForm()
    return render(request, 'new_post.html', {'form': form})

def postcomment(request, blog_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = Author.objects.get(user=request.user.id)
            blog = Blog.objects.get(id=blog_pk)
            comment = form.cleaned_data.get('comment_text')
            new_comment = Comment.objects.create(author=author, comment=comment, blog=blog)
            return redirect(reverse('blog-detail', args=[int(blog_pk)]))
    else:
        form = CommentForm()
    return render(request, 'blog_detail.html', {'form': form})