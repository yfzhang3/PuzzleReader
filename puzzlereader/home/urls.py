from django.urls import path

from . import views
from .views import BookList, BookDetail

urlpatterns = [
    path('', BookList.as_view(), name='book'),
    path('okay /<int:pk>/', BookDetail.as_view(), name='books'),
]
