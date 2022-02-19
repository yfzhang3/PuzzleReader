from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def home_view(request):
    return render(request, 'home/home_v.html')
