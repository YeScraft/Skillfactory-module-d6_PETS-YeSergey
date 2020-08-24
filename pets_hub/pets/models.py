from django.db import models
from django.core import validators
# from datetime import date
# Create your models here.

class PetType(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    TYPE_PET = [(DOG, 'dog'), (CAT, 'cat'), (PARROT, 'parrot')]

    type = models.CharField(max_length=90, choices=TYPE_PET, verbose_name='Вид')
    breed = models.CharField(max_length=255, verbose_name='Порода')

    def __str__(self):
        return "-".join((str(self.type), str(self.breed),))


class Pet(models.Model):

    pet_type = models.ForeignKey('PetType', on_delete=models.CASCADE, verbose_name='Животина')
    pet_name = models.CharField(max_length=100, verbose_name='Кличка',)
    age = models.IntegerField(verbose_name="Возраст", validators=[validators.MaxValueValidator(300)])
    description = models.TextField(verbose_name="Описание")
    reg_date = models.DateField(auto_now_add=False, verbose_name='Дата регистрации')
    photo = models.ImageField(upload_to='pets_photo', blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.pet_name

