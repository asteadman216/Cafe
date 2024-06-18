from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeaListView.as_view(), name='tea_list'),
    path('', views.TeaCreateView.as_view(), name='add_tea'),
    path('<int:pk>/', views.TeaDetailView.as_view(), name='tea_detail'),
    path('<int:pk>/update/', views.TeaUpdateView.as_view(), name='update_tea'),
    path('<int:pk>/delete/', views.TeaDeleteView.as_view(), name='delete_tea')
]