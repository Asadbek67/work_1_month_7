from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Food
from .forms import FoodForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
    foods = Food.objects.all()[:5]
    return render(request, 'home.html', {'foods': foods})

def all_foods(request):
    foods = Food.objects.all()
    return render(request, 'all_food.html', {'foods': foods})

def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    return render(request, 'food_detail.html', {'food': food})

def category_foods(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    foods = Food.objects.filter(category=category)
    return render(request, 'category_foods.html', {'category': category, 'foods': foods})

def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_foods')
    else:
        form = FoodForm()
    return render(request, 'add_food.html', {'form': form})

def edit_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_detail', food_id=food.id)
    else:
        form = FoodForm(instance=food)
    return render(request, 'edit_food.html', {'form': form, 'food': food})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})