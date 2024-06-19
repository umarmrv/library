from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BooksSerializer


def index(request):
    books = Books.objects.all()
    return HttpResponse(b for b in books)


class BooksView(CreateAPIView):
    serializer_class = BooksSerializer


class BooksList(ListAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()


class BooksDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
