from django.shortcuts import render, get_object_or_404
from .models import Author, Post
from .forms import AuthorForm, PostForm, EditorialForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/success.html', {'message': 'Author added!'})
    else:
        form = AuthorForm()
    return render(request, 'blog/form.html', {'form': form, 'title': 'Add Author'})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/success.html', {'message': 'Post added!'})
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {'form': form, 'title': 'Add Post'})

def search_posts(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query) if query else None
    return render(request, 'blog/search.html', {'results': results, 'query': query})

def add_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/success.html', {'message': 'Editorial agregada exitosamente'})
    else:
        form = EditorialForm()
    return render(request, 'blog/form.html', {'form': form, 'title': 'Agregar Editorial'})