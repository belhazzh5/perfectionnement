import json
from fomrulaire.models import Famille

def import_data_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        for entry in data:
            famille_instance = Famille(
                age=entry['age'],
                nb=entry['nb'],
                creation_date=entry['creation_date'],
                nom=entry['nom'],
                prenom=entry['prenom'],
                date=entry['date'],
                adress=entry['adress'],
                phone1=entry['phone1'],
                phone2=entry['phone2'],
                etat_civil=entry['etat_civil'],
                etat_santé=entry['etat_santé'],
                nb_enfants_scolaire=entry['nb_enfants_scolaire'],
                nb_enfants_chomeur=entry['nb_enfants_chomeur'],
                nb_enfants_handicapés=entry['nb_enfants_handicapés'],
                nb_enfants_totales=entry['nb_enfants_totales'],
                comme_familles=entry['comme_familles'],
                revenu_total=entry['revenu_total'],
                couverture_social=entry['couverture_social'],
                couverture_social_liste=entry['couverture_social_liste'],
                local=entry['local'],
                etat_local=entry['etat_local'],
                depense=entry['depense'],
                evaluation=entry['evaluation']
            )
            famille_instance.save()

if __name__ == "__main__":
    json_file_path = "data.json"
    import_data_from_json(json_file_path)
