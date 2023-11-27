from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'My Store - Главная'
    }
    return render(request, 'catalog/index.html', context)


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
