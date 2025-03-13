from django.http import Http404
from django.shortcuts import render, get_object_or_404

from main.models import Car, Sale


def cars_list_view(request):
    cars = Car.odjects(all)# получите список авто
    template_name = 'main/list.html'
    return render(request, template_name, {'cars': cars})  # передайте необходимый контекст


def car_details_view(request, car_id):
    car = get_object_or_404(Car, id = car_id)# получите авто, если же его нет, выбросьте ошибку 404
    template_name = 'main/details.html'
    return render(request, template_name, {'car': car})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        car = get_object_or_404(Car, id=car_id)
        sales = Sale.objects.filter(car=car)# получите авто и его продажи
        template_name = 'main/sales.html'
        return render(request, template_name, {'car': car, 'sales': sales})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')

