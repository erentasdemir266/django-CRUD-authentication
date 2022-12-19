from django.shortcuts import render,get_object_or_404,redirect,Http404
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='accounts/login')
def index(request):
    Post_List=Post.objects.all()
    query=request.GET.get('q')
    if query:
        Post_List=Post_List.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) 
        ).distinct()
    paginator = Paginator(Post_List, 5) # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'blog/index.html',{'posts':posts})


def detail(request,slug):
    post=get_object_or_404(Post,slug=slug)
    form=CommentForm(request.POST or None)
    if form.is_valid():
        comment= form.save(commit=False)
        comment.post=post
        comment.save()
    context={'post':post,'form':form,}
    return render(request,'blog/detail.html',context)



def create(request):
    if not request.user.is_authenticated:
        return Http404()
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post= form.save(commit=False)
        post.user=request.user
        post.save()
        messages.success(request,'Başarılı bir şekilde oluşturdunuz')
        return redirect('index')
    context={'form':form}
    return render(request,'blog/form.html',context)


def update(request,slug):
    if not request.user.is_authenticated:
        return Http404()
    post=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None,request.FILES or None,instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,'Başarılı bir şekilde güncellediniz')
        return redirect('index')
    context={'form':form}

    return render(request,'blog/form.html',context)



def delete(request,slug):
    if not request.user.is_authenticated:
        return Http404()
    post=get_object_or_404(Post,slug=slug)
    post.delete()
    return redirect('index')
