# Generated by Django 4.0.4 on 2022-05-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predmeti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('kod', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
                ('ects', models.IntegerField()),
                ('sem_red', models.IntegerField()),
                ('sem_izv', models.IntegerField()),
                ('izborni', models.CharField(choices=[('DA', 'da'), ('NE', 'ne')], max_length=50)),
            ],
        ),
    ]
