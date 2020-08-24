from django.contrib import admin
from .models import PetType, Pet
# Register your models here.

@admin.register(PetType)
class PetTypeAdmin(admin.ModelAdmin):

    list_display = ('type', 'breed',)
    # fields = ('type', 'breed',)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

    list_display = ('pet_type', 'pet_name')

