from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BooksList.as_view()),
    path('books/<int:pk>/', views.BooksDetail.as_view()),
    path('books/create/', views.BooksView.as_view()),
    path('books/<int:pk>/update/', views.BooksDetail.as_view()),
    path('books/<int:pk>/delete/', views.BooksDetail.as_view()),
]
