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
    """Передаем данные из БД на страницу расчета ТЭП"""

    context = {}
    context['Equipment'] = Equipment.objects.all()
    context['Material'] = Material.objects.all()
    context['Product'] = Product.objects.all()
    context['Equipment_l'] = Equipment.objects.filter(genus='tipe1')
    context['Equipment'] = Equipment.objects.all()
    context['Equipment_s'] = Equipment.objects.filter(genus='tipe3')
    context['Equipment_d'] = Equipment.objects.filter(genus='tipe2')

    return render(request, 'main.html', context=context)


def calculate_page(request):
    if request.POST:
        wages = {
            'drob':114,
            'sush':114,
            'lit':205
        }
        energy_price = 4.82
        context = {}


        context['product'] = request.POST['product']
        context['m1'] = request.POST['m1']
        context['m2'] = request.POST['m2']
        context['count'] = request.POST['count']
        context['g'] = request.POST['g']
        context['eq_l'] = request.POST['eq_l']
        context['eq_s'] = request.POST['eq_s']
        context['eq_d'] = request.POST['eq_d']
        context['time_s'] = request.POST.get('time_s', '0')
        context['time_d'] = request.POST.get('time_d', '0')
        context['temp'] = request.POST.get('temp', '0')
        context['count_1'] = request.POST.get('count_1', '90')
        context['count_2'] = request.POST.get('count_2', '10')

        product = Product.objects.get(name=context['product'])

        weight_product = float(context['count'])*(int(product.net_weight)/1000)

        material1 = Material.objects.get(commodities=context['m1'])
        material2 = Material.objects.get(commodities=context['m2'])
        context ['price_product'] = (weight_product * float(context['count_1'])/100 * int(material1.price)
                                     + weight_product * float(context['count_2'])/100 * int(material2.price))

        price_s = int(context['time_s']) * energy_price * 4.37
        context['price_s'] = round(price_s, 2)

        price_d = int(context['time_d']) * energy_price * 15
        context['price_d'] = round(price_d, 2)

        wages_drob = wages['drob'] * int(context['time_d'])
        context['wages_drob'] = round(wages_drob, 2)

        wages_sush = wages['sush'] * int(context['time_s'])
        context['wages_sush'] = round(wages_sush, 2)

        wages_lit = wages['lit'] * 18
        context['wages_lit'] = round(wages_lit, 2)

        sum= wages_lit + wages_sush + wages_drob + price_d + price_s + \
             float(context['price_product']) +4095 +673 +1998 +131 + 1034
        context['sum'] = round(sum, 2)

        price_unit = sum / int(context['count'])
        context['price_unit'] = round(price_unit, 2)


    return render(request, 'calculate.html', context=context)


class ManufacturerAddView(CreateView):
    model = Manufacturer
    template_name = 'manufacturer_add.html'
    form_class = ManufacturerAddForm


    def get_context_data(self, **kwargs):
        """передаем свой контекст"""
        context = super().get_context_data(**kwargs)
        kwargs['manufaturer_list'] = Manufacturer.objects.all()
        return context