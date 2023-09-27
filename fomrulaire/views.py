from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Famille
from .forms import FamilleForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Import your custom form

class FamilleListView(LoginRequiredMixin,ListView):
    model = Famille
    template_name = 'famille_list.html'
    context_object_name = 'familles'
    
@login_required()
def index(request):
    return render(request,'fomrulaire/index.html')

class FamilleCreateView(LoginRequiredMixin,CreateView):
    model = Famille
    form_class = FamilleForm
    template_name = 'famille_form.html'
    success_url = reverse_lazy('famille_list')

class FamilleUpdateView(LoginRequiredMixin,UpdateView):
    model = Famille
    form_class = FamilleForm
    template_name = 'famille_form.html'
    success_url = reverse_lazy('famille_list')

class FamilleDeleteView(LoginRequiredMixin,DeleteView):
    model = Famille
    template_name = 'famille_confirm_delete.html'
    success_url = reverse_lazy('famille_list')

def dash(request):
    return render(request,'fomrulaire/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect('index')  # Redirect to your desired page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def not_found(request):
    return render(request,'404.html')