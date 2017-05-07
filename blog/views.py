from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.views import login as auth_login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Post
from .forms import PostForm

def login(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('loggedin'))
    else:
        return auth_login(request, *args, **kwargs)

def loggedIn(request):
    if request.user.is_authenticated():
        return render(request, 'loggedin.html', {'user': request.user.username})
    else:
        return HttpResponseRedirect(reverse('login'))

def viewAllPosts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'index.html', {'posts': posts})

def viewOnePost(reqest, pk):
    post = Post.objects.get(pk=pk)
    return render(reqest, 'viewPost.html', {'post': post})

def writePost(request):
    if request.user.is_authenticated():
        if request.method == "GET":
            form = PostForm()
        elif request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect('viewOnePost', pk=obj.pk)
                
        ctx = {
            'form': form,
        }
        return render(request, 'writePost.html', ctx)
        
    else:
        return HttpResponseRedirect(reverse('login'))

def editPost(request, pk):
    post = Post.objects.get(pk=pk)
    if post.user.id == request.user.id:
        if request.method == "GET":
            form = PostForm(instance=post)
        elif request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                return redirect('viewOnePost', pk=obj.pk)
        ctx = {
            'form': form,
            'post': post,
        }
        return render(request, 'editPost.html', ctx)
        
    else:
        return HttpResponseRedirect(reverse('home'))

def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    if post.user.id == request.user.id:
        post.delete()
    return HttpResponseRedirect(reverse('home'))
