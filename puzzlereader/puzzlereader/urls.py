from django.contrib import admin
from django.urls import include, path
from home.views import home_view

urlpatterns = [
    path('', home_view, name=''),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
