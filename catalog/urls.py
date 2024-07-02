# catalog/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', LoginView.as_view(template_name='catalog/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('coffee-menu/', views.coffee_menu, name='coffee_menu'),
    path('tea-menu/', views.tea_menu, name='tea_menu'),
    path('kids-menu/', views.kids_menu, name='kids_menu'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
    path('payment/', views.payment, name='payment'),
]