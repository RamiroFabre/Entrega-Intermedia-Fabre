# Generated by Django 4.1.2 on 2022-11-04 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Filtro',
        ),
    ]
