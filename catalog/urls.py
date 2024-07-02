# catalog/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views
# from .views import CustomPasswordResetDoneView


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
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]