from django.urls import path
from . import views

urlpatterns = [
    path('', views.KidsListView.as_view(), name='kids_list'),
    path('', views.KidsCreateView.as_view(), name='add_kids'),
    path('<int:pk>/', views.KidsDetailView.as_view(), name='kids_detail'),
    path('<int:pk>/update/', views.KidsUpdateView.as_view(), name='update_kids'),
    path('<int:pk>/delete/', views.KidsDeleteView.as_view(), name='delete_kids')
]