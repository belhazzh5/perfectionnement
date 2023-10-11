from django.urls import path
from .views import FamilleListView, FamilleCreateView, FamilleUpdateView, FamilleDeleteView,dash,register,dash,not_found

urlpatterns = [
    path('404/', not_found, name='not-found'),
    path('', dash, name='famille_list'),
    path('index/', FamilleListView.as_view(), name='index'),
    path('profile/', dash, name='profile'),
    path('accounts/register/', register, name='register'),
    path('create/', FamilleCreateView.as_view(), name='famille_create'),
    path('update/<int:pk>/', FamilleUpdateView.as_view(), name='famille_update'),
    path('delete/<int:pk>/', FamilleDeleteView.as_view(), name='famille_delete'),
]
