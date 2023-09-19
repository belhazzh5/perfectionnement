from django import forms
from .models import Famille

class FamilleForm(forms.ModelForm):
    class Meta:
        model = Famille
        fields = ['image','creation_date','nom', 'prenom', 'date', 'adress', 'phone1', 'phone2', 'etat_civil', 'etat_santé',
                  'nb_enfants_scolaire', 'nb_enfants_chomeur', 'nb_enfants_handicapés', 'nb_enfants_totales',
                  'comme_familles', 'revenu_total', 'couverture_social', 'couverture_social_liste',
                  'local', 'etat_local', 'depense', 'evaluation','nb']
        widgets = {
                    'creation_date' : forms.DateInput(attrs={'type': 'date'}),
                    'date' : forms.DateInput(attrs={'type': 'date'}),
                    'depense': forms.CheckboxSelectMultiple(),
                    'couverture_social': forms.RadioSelect(),
                }
