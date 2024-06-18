from django.contrib import admin
from django.urls import path, include
from catalog import views as catalog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog_views.home, name='home'),  # Root URL pattern
    path('coffees/', include('catalog.urls_coffee')),
    path('teas/', include('catalog.urls_teas')),
    path('kids/', include('catalog.urls_kids')),
]


