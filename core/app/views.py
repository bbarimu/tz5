from django.shortcuts import render
from .models import Post, Author, Category
from .forms import PostForm, CategoryForm, AuthorForm

def post_list(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'app/post_list.html', context)


def post_detail(request, pk):

    post = Post.objects.filter(pk = pk).first()

    return render(request, 'app/post.html', context={'post': post})

    
def post_create(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request, 'app/post_create.html',{'form': form, 'authors': authors, 'categories': categories})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:    
        form = CategoryForm()
    return render(request, 'app/category_form.html', {'form': form})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm()
    return render(request, 'app/author_form.html', {'form': form})
