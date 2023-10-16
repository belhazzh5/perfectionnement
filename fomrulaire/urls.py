from django.urls import path
from .views import FamilleListView, FamilleCreateView, FamilleUpdateView, FamilleDeleteView,register,not_found
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('404/', not_found, name='not-found'),
    path('', LoginView.as_view(), name='login'),
    path('index/', FamilleListView.as_view(), name='index'),
    path('accounts/register/', register, name='register'),
    path('create/', FamilleCreateView.as_view(), name='famille_create'),
    path('update/<int:pk>/', FamilleUpdateView.as_view(), name='famille_update'),
    path('delete/<int:pk>/', FamilleDeleteView.as_view(), name='famille_delete'),
]
