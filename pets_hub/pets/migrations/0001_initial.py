# Generated by Django 2.2.6 on 2020-08-23 14:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('dog', 'dog'), ('cat', 'cat'), ('parrot', 'parrot')], max_length=90, verbose_name='Вид')),
                ('breed', models.CharField(max_length=255, verbose_name='Порода')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=100, verbose_name='Кличка')),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(300)], verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('reg_date', models.DateField(verbose_name='Дата регистрации')),
                ('photo', models.ImageField(blank=True, upload_to='pets_photo', verbose_name='Фотография')),
                ('pet_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.PetType', verbose_name='Животина')),
            ],
        ),
    ]