# Generated by Django 3.2.3 on 2021-05-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mot_de_passe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mot', models.CharField(max_length=100)),
                ('indice_1', models.CharField(max_length=100)),
                ('indice_2', models.CharField(max_length=100)),
                ('indice_3', models.CharField(max_length=100)),
            ],
        ),
    ]
