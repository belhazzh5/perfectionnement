from django.urls import path
from .views import FamilleListView, FamilleCreateView, FamilleUpdateView, FamilleDeleteView,index,dash,register,not_found

urlpatterns = [
    path('404/', not_found, name='not-found'),
    path('', FamilleListView.as_view(), name='famille_list'),
    path('index/', index, name='index'),
    path('profile/', dash, name='profile'),
    path('accounts/register/', register, name='register'),
    path('create/', FamilleCreateView.as_view(), name='famille_create'),
    path('update/<int:pk>/', FamilleUpdateView.as_view(), name='famille_update'),
    path('delete/<int:pk>/', FamilleDeleteView.as_view(), name='famille_delete'),
]
