from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Film, History
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm


def home_page(request):
    categories = Category.objects.all()
    films = Film.objects.all() [:4]

    context = {
        'categories': categories,
        'films': films 
    }

    return render(request, "./home.html", context)

def films_page(request):
    films = Film.objects.all() [:4]
    context = {
        'films': films 
    }
    return render(request, "./films.html", context)

def categories_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories 
    }
    return render(request, "./categories.html", context)

def histories_page(request):
    histories = History.objects.all()
    context = {
        'histories': histories 
    }
    return render(request, "./histories.html", context)

def film_detail_page(request, pk):
    film = get_object_or_404(Film, pk=pk)
    context = {
        'film': film
    }
    return render(request, "./film-detail.html", context)

def history_detail_page(request, pk):
    history = get_object_or_404(History, pk=pk)
    context = {
        'history': history
    }
    return render(request, "./history-detail.html", context)

def films_by_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    films = Film.objects.filter(category=category)
    context = {
        'category' : category,
        'films': films
    }
    return render(request, "./films-by-category.html", context)

def sigh_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form .is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, "./sign-up.html", context)

def login_page(request): 
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()

    context = {
        'form': form 
    }
    return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect("home_page")