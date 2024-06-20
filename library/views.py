# from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from rest_framework import generics
from .serializers import BookSerializer


def index(request):
    books = Book.objects.all()
    return HttpResponse(b for b in books)


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.order_by('-id')
    serializer_class = BookSerializer


# class BooksList(generics.ListAPIView):
 #   serializer_class = BooksSerializer
 #   queryset = Books.objects.all()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.order_by('-id')
