from django.contrib import admin
from django.urls import path
from .views import Index, PetList, PetView, Contacts, About, PetTypeCreate, PetCreate


app_name = 'pets'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('pets/', PetList.as_view(), name='pet_list'),
    path('pets/<int:pk>/', PetView.as_view(), name='pet_details'),
    path('pets/create/', PetTypeCreate.as_view(), name='pet_type_create'),
    path('pets/create/pet/', PetCreate.as_view(), name='pet_create'),
    path('contacts/', Contacts.as_view()),
    path('about/', About.as_view()),
    ]

