from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from .models import *
from .forms import *


# Create your views here.


def main_page(request):
    return render(request, 'main.html')


class ManufacturerAddView(CreateView):
    model = Manufacturer
    template_name = 'manufacturer_add.html'
    form_class = ManufacturerAddForm

    def get_context_data(self, **kwargs):
        """передаем свой контекст"""
        kwargs['manufaturer_list'] = Manufacturer.objects.all()
        return super().get_context_data(**kwargs)