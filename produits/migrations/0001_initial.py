# Generated by Django 4.2.7 on 2023-11-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('reference', models.CharField(max_length=20)),
                ('pointure', models.FloatField(default=0)),
                ('photo', models.CharField(max_length=500)),
            ],
        ),
    ]
