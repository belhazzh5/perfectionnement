# Generated by Django 4.1 on 2023-10-19 19:06

from django.db import migrations, models
import fomrulaire.models


class Migration(migrations.Migration):

    dependencies = [
        ('fomrulaire', '0011_logs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famille',
            name='adress',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='famille',
            name='couverture_social',
            field=models.TextField(blank=True, choices=[('y', 'نعم'), ('n', 'لا')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='famille',
            name='depense',
            field=models.CharField(blank=True, choices=[('a', 'مصاريف علاج'), ('b', 'مصاريف دراسة '), ('c', 'خلاص الماء '), ('d', 'كهرباء '), ('e', 'معلوم الكراء')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='famille',
            name='etat_civil',
            field=models.CharField(blank=True, choices=[('a', 'أعزب/عزباء'), ('b', 'متزوج/متزوجة'), ('c', 'مطلق/مطلقة')], default='a', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='famille',
            name='nom',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='famille',
            name='phone1',
            field=models.CharField(blank=True, max_length=8, null=True, validators=[fomrulaire.models.is_number]),
        ),
        migrations.AlterField(
            model_name='famille',
            name='prenom',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
