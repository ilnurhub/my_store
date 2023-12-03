from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'My Store - Главная'
    }


def contacts(request):
    context = {
        'title': 'My Store - Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nНомер телефона: {phone}\nСообщение: {message}')
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object': Product.objects.get(id=pk),
        'title': product_item.name
    }
    return render(request, 'catalog/product.html', context)
