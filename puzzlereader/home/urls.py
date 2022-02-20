from django.urls import path

from . import views
from .views import BookCreate, BookList, BookDetail

app_name = "home"
urlpatterns = [
    path('books/', BookList.as_view(), name='books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book'),
    path('books/create/', BookCreate.as_view(), name='create')
]
