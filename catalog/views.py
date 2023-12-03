from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = product_item.name
        return context_data
