# Generated by Django 3.2.3 on 2021-05-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mot_de_passe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
