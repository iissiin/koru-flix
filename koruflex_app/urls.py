from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('films/', views.films_page, name='films_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('histories/', views.histories_page, name='histories_page'),
    path('films/detail/<int:pk>/', views.film_detail_page, name = 'film_detail_page'),
    path('history/detail/<int:pk>/', views.history_detail_page, name = 'history_detail_page'),
    path('category/films/<slug:slug>/', views.films_by_category_page, name='films_by_category_page'),
    path('sign-up/', views.sigh_up_page, name='sign_up_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_action')
]
