from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
from .models import Book

#from puzzlereader.home.models import Book


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def home_view(request):
    return render(request, 'home/home_v.html')


class BookList(ListView):
    model = Book
    context_object_name = 'books'


class BookDetail(DetailView):
    model = Book
    # looking for task_detail
