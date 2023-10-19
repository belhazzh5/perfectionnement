from django.db import models
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.
def is_number(value):
    return value.isnumeric()
phone_number_validator = RegexValidator(
    regex=r'^[0-9]*$',
    message='Phone number must contain only numeric digits.',
)

    
class Logs(models.Model):
    description = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Famille(models.Model):
    image = models.ImageField(upload_to="images/familles",blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    nb = models.BigIntegerField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    CIVIL = (("a","أعزب/عزباء"),("b","متزوج/متزوجة") ,("c","مطلق/مطلقة"))
    SANTE = (("a","صحة جيدة"),("b","معاق") ,("c","مرض مزمن "))
    FAMILLE = (("a","الأب والأم"),("b","الخال أو الخالة") ,("c","العم أو العمة "),('d',"أخر"))
    REVENUE = (("a","راتب الشهري "),("b","منحة") )
    SOCIAL = (("a","راتب الشهري "),("b","منحة") )
    LOCAL = (("a","ملكية فردية"),("b","ملكية فردية") )
    ETAT_LOCAL = (("a","مكتمل البناء "),("b","مكتمل البناء") )
    GENRES_CHOICES = (("a","مصاريف علاج"),("b","مصاريف دراسة ") , ("c","خلاص الماء ") , ("d","كهرباء "), ("e","معلوم الكراء"))
    GRADE = (("a","راتب الشهري "),("b","منحة") )
    nom = models.CharField(max_length=70,null=True,blank=True)
    prenom = models.CharField(max_length=70,null=True,blank=True)
    date = models.DateField()
    adress = models.CharField(max_length=70,null=True,blank=True)
    phone1 = models.CharField(max_length=8,validators=[is_number],null=True,blank=True)
    phone2 = models.CharField(max_length=8,validators=[is_number],blank=True, null=True)
    etat_civil = models.CharField(
        max_length=1,
        choices=CIVIL,
        blank=True,
        default='a',
        null=True
    )
    etat_santé = models.CharField(
        max_length=1,
        choices=SANTE,
        blank=True,
        default='b',
    )
    nb_enfants_scolaire = models.IntegerField(blank=True, null=True,default=0) 
    nb_enfants_chomeur = models.IntegerField(blank=True, null=True,default=0) 
    nb_enfants_handicapés = models.IntegerField(blank=True, null=True,default=0) 
    nb_enfants_totales = models.IntegerField(blank=True, null=True,default=0) 
    comme_familles =  models.CharField(
        max_length=1,
        choices=FAMILLE,
        blank=True,
        default='a',
    )
    revenu_total =  models.CharField(
        max_length=1,
        choices=REVENUE,
        blank=True,
        default='a',
    )
    couverture_social = models.TextField(max_length=1,choices=[("y","نعم"),("n","لا")],null=True,blank=True)

    couverture_social_liste = models.CharField(
        max_length=1,
        choices=SOCIAL,
        blank=True,
        default='y',
    )
    local = models.CharField(
        max_length=1,
        choices=LOCAL,
        blank=True,
        default='a',
    )
    etat_local = models.CharField(
        max_length=1,
        choices=LOCAL,
        blank=True,
        default='a',
    )

    depense = models.CharField(choices=GENRES_CHOICES,max_length=5,null=True,blank=True)
    evaluation = models.TextField(choices=GRADE,max_length=1,default="a")

    def __str__(self):
        return f"{self.nom} {self.prenom}"