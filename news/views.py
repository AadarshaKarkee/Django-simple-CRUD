from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import News, NewsCategory
from .forms import NewsAddForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def news_list(request):
    news = News.objects.all()
    category = NewsCategory.objects.all()
    context={
        "news":news,
        "category":category
    }
    return render(request, 'index.html', context)


def news_detail(request, id, slug):
    news = News.objects.get(id=id)
    category = NewsCategory.objects.all()
    context={
        "news":news,
        "category":category
    }
    return render(request, 'detail.html', context)

def news_category(request, id):
    news = News.objects.filter(category=id)
    category = NewsCategory.objects.all()
    context={
        "news":news,
        "category":category
    }
    return render(request, 'index.html', context)

@login_required(login_url='/admin')
def news_create(request):
    category = NewsCategory.objects.all()
    form = NewsAddForm()
    if request.method == "POST":
        form = NewsAddForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context={
        "form":form,
        "category":category
    }
    return render(request, 'addNews.html',context)

@login_required(login_url='/admin')
def news_delete(request,id):
    news = get_object_or_404(News, id=id)
    if request.method == "POST":
        news.delete()
        return redirect("/")
    return render(request, 'Newsdelete.html')

@login_required(login_url='/admin')
def news_update(request, id):
    category = NewsCategory.objects.all()
    news = get_object_or_404(News, id=id)
    form = NewsAddForm(instance=news)
    if request.method == "POST":
        form = NewsAddForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
        return redirect("/")
    context={
        "form":form,
        "category":category
    }
    return render(request, 'addNews.html',context)
