from django.contrib import admin
from django.urls import include, path
from home.views import home_view, BookList
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('home/', include('home.urls')),
#path('books/', include('home.urls'), name="home"),
