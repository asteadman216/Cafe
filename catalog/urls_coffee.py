from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoffeeListView.as_view(), name='coffee_list'),
    path('', views.CoffeeCreateView.as_view(), name='add_coffee'),
    path('<int:pk>/', views.CoffeeDetailView.as_view(), name='coffee_detail'),
    path('<int:pk>/update/', views.CoffeeUpdateView.as_view(), name='update_coffee'),
    path('<int:pk>/delete/', views.CoffeeDeleteView.as_view(), name='delete_coffee')
]