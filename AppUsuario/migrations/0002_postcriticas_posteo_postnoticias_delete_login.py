# Generated by Django 4.1.3 on 2022-11-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCriticas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90)),
                ('sub_titulo', models.CharField(max_length=90)),
                ('fecha', models.DateField()),
                ('texto', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90)),
                ('fecha', models.DateField()),
                ('texto', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PostNoticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90)),
                ('sub_titulo', models.CharField(max_length=90)),
                ('fecha', models.DateField()),
                ('texto', models.CharField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
