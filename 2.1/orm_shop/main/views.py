from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    query = request.GET.get("q", "")
    print(query)
    cars = Car.objects.filter(model__icontains=query)
    template_name = 'main/list.html'
    return render(request, template_name, {"cars": cars, "query":query})  # передайте необходимый контекст


def car_details_view(request, car_id):
    car = Car.objects.get(pk=car_id)
    template_name = 'main/details.html'
    return render(request, template_name, {"car": car})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        sales = Sale.objects.filter(car=car_id)
        car = sales[0].car.get()
        sales_dict = []
        for sale in sales:
            sales_dict.append({
                "client": sale.client.get(),
                "created_at": sale.created_at
            })
        template_name = 'main/sales.html'

        context = {
            "car": car,
            "sales": sales_dict
        }

        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')
