from django.shortcuts import render, reverse, redirect
from django.template import loader

from .models import Pet, PetType
from .forms import PetForm, PetTypeForm

# from django.forms import formset_factory

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, TemplateView

from django.urls import reverse_lazy

# from django.http.response import HttpResponseRedirect


# Create your views here.


class Index(ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'index.html'


class PetList(ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet_list.html'


class PetView(DetailView):
    model = Pet
    context_object_name = 'pet'
    template_name = 'pet_details.html'


class PetTypeCreate(CreateView):
    model = PetType
    form_class = PetTypeForm
    template_name = 'pettype_edit.html'
    success_url = reverse_lazy('pets:pet_create')

class PetCreate(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet_edit.html'
    success_url = reverse_lazy('pets:index')

# def is_save(author_form):
#     try:
#         author_form.save()
#         return True
#     except BaseException:
#         return False

# def petcreate(request):
#     if request.method == 'POST':
#         type_form = PetTypeForm(request.POST, request.FILES, prefix='type')
#         pet_form = PetForm(request.POST, request.FILES, prefix='pet')
#         if type_form.is_valid() and pet_form.is_valid():
#             r = type_form.save(commit=False)
#             # do stuff, e.g. setting any values excluded in the MainForm
#             pet_form.save()
#             r.save()
#             return HttpResponseRedirect('pets:index')
#     # type_form = PetTypeForm(instance=main, prefix='type')
#     # pet_form = PetForm(instance=main, prefix='pet')
#     extra_context = {
#         'type_form': PetTypeForm(prefix='type'),
#         'pet_form': PetForm(prefix='pet')
#     }
#     return render(request, 'pettype_edit.html', extra_context)

# def petcreate(request):
#     if request.method == 'POST':
#         type_form = PetTypeForm(request.POST, request.FILES, prefix='type')
#         pet_form = PetForm(request.POST, request.FILES, prefix='pet')
#         if type_form.is_valid() and pet_form.is_valid():
#             if is_save(pet_form):
#                 return HttpResponseRedirect(reverse_lazy('pets:index'))
#             else:
#                 return HttpResponseRedirect(reverse_lazy('pets:index'))
#             return HttpResponseRedirect(reverse('pets:index'))
#     extra_context = {
#         'type_form': PetTypeForm(prefix='type'),
#         'pet_form': PetForm(prefix='pet')
#     }
#     return render(request, 'pettype_edit.html', extra_context)


class About(TemplateView):
    template_name = 'about.html'


class Contacts(TemplateView):
    template_name = 'contacts.html'
