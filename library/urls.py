from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookView.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
    path('book/create/', views.BookView.as_view()),
    path('book/<int:pk>/update/', views.BookDetail.as_view()),
    path('book/<int:pk>/delete/', views.BookDetail.as_view()),
]
