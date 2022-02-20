from django.contrib import admin
from django.urls import include, path
from home.views import home_view, BookList


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]

#path('home/', include('home.urls')),
#path('books/', include('home.urls'), name="home"),
