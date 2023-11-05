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
from django.db.models import Count
from .models import Logs
class FamilleListView(LoginRequiredMixin,ListView):
    model = Famille
    template_name = 'fomrulaire/index.html'
    context_object_name = 'familles'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Basic statistics
        context['families'] = Famille.objects.all()
        context['total_families'] = Famille.objects.count()
        context['civil_status_counts'] = Famille.objects.values('etat_civil').annotate(count=Count('id'))
        context['health_status_counts'] = Famille.objects.values('etat_santé').annotate(count=Count('id'))

        # Filtered lists (example: families with more than 3 children)
        context['families_with_many_children'] = Famille.objects.filter(nb_enfants_totales__gt=3)

        # Recent activities (example: latest 5 additions)
        context['recent_additions'] = Famille.objects.order_by('-creation_date')[:5]
        enfants = 0
        nb_enfants_handicapés = []
        nb_enfants_scolaire = []
        nb_enfants_chomeur = []
        for famille in Famille.objects.all():
            enfants += famille.nb_enfants_totales
            nb_enfants_handicapés.append(famille.nb_enfants_handicapés)
            nb_enfants_chomeur.append(famille.nb_enfants_chomeur)
            nb_enfants_scolaire.append(famille.nb_enfants_scolaire)
        context['enfants'] = int (enfants / Famille.objects.count())
        context['nb_enfants_scolaire'] = nb_enfants_scolaire
        context['nb_enfants_chomeur'] = nb_enfants_chomeur
        context['nb_enfants_handicapés'] = nb_enfants_handicapés
        # Static content
        context['logs'] = Logs.objects.all()

        return context
        

class FamilleCreateView(LoginRequiredMixin,CreateView):
    model = Famille
    form_class = FamilleForm
    template_name = 'famille_form.html'
    success_url = reverse_lazy('famille_list')


class FamilleUpdateView(LoginRequiredMixin,UpdateView):
    model = Famille
    form_class = FamilleForm
    template_name = 'famille_form_update.html'
    success_url = reverse_lazy('famille_list')

class FamilleDeleteView(LoginRequiredMixin,DeleteView):
    model = Famille
    template_name = 'famille_confirm_delete.html'
    success_url = reverse_lazy('famille_list')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            return redirect('index')  # Redirect to your desired page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def not_found(request):
    return render(request,'404.html')

class FamillelistView(LoginRequiredMixin,ListView):
    model = Famille
    template_name = 'famille_list.html'
    context_object_name = 'myFamily'

