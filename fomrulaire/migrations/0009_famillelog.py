# Generated by Django 4.1 on 2023-09-27 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fomrulaire', '0008_alter_famille_nb_enfants_chomeur_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilleLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fomrulaire.famille')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
