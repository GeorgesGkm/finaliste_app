# Generated by Django 5.0.1 on 2024-02-07 11:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('postnom', models.CharField(max_length=255)),
                ('sexe', models.CharField(choices=[('1', 'M'), ('2', 'F')], max_length=10)),
                ('promotion', models.CharField(choices=[('1', 'L2 II'), ('2', 'L2 CSI'), ('3', 'LPTA 4 II')], max_length=10)),
                ('departement', models.CharField(choices=[('1', 'INFORMATIQUE'), ('2', 'GESTION')], max_length=10)),
                ('langage', models.CharField(max_length=255)),
                ('directeur', models.CharField(max_length=255)),
                ('codirecteur', models.CharField(max_length=255)),
                ('sujet', models.TextField()),
                ('problematique', models.TextField()),
                ('date_depot', models.DateField(auto_now=True)),
            ],
        ),
    ]
