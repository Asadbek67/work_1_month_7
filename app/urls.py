from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.all_foods, name='home'),
    path('foods/', views.all_foods, name='all_foods'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('category/<int:category_id>/', views.category_foods, name='category_foods'),
    path('food/add/', views.add_food, name='add_food'),
    path('food/edit/<int:food_id>/', views.edit_food, name='edit_food'),
    path('add-food/', views.add_food, name='add-food'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
]