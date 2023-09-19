from django.urls import path
from .views import FamilleListView, FamilleCreateView, FamilleUpdateView, FamilleDeleteView

urlpatterns = [
    path('', FamilleListView.as_view(), name='famille_list'),
    path('create/', FamilleCreateView.as_view(), name='famille_create'),
    path('update/<int:pk>/', FamilleUpdateView.as_view(), name='famille_update'),
    path('delete/<int:pk>/', FamilleDeleteView.as_view(), name='famille_delete'),
]
