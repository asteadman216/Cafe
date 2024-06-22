from django.contrib import admin
from django.urls import path, include
from catalog import views as catalog_views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('coffees/', include('catalog.urls_coffee')),
    path('teas/', include('catalog.urls_teas')),
    path('kids/', include('catalog.urls_kids')),
    path('catalog/', include('catalog.urls')),  # Include your app's URLs
    path('register/', include('register.urls')),
]
