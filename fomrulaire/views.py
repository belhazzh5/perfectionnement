from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Famille
from .forms import FamilleForm

class FamilleListView(ListView):
    model = Famille
    template_name = 'famille_list.html'
    context_object_name = 'familles'

class FamilleCreateView(CreateView):
    model = Famille
    form_class = FamilleForm
    template_name = 'famille_form.html'
    success_url = reverse_lazy('famille_list')

class FamilleUpdateView(UpdateView):
    model = Famille
    form_class = FamilleForm
    template_name = 'famille_form.html'
    success_url = reverse_lazy('famille_list')

class FamilleDeleteView(DeleteView):
    model = Famille
    template_name = 'famille_confirm_delete.html'
    success_url = reverse_lazy('famille_list')
