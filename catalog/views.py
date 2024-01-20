from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import OwnerProductForm, VersionForm, ModeratorProductForm, FullProductForm
from catalog.models import Product, Version, Category


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'My Store - Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()[:3]
        return context_data


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    extra_context = {
        'title': 'My Store - Категории продуктов'
    }


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    extra_context = {
        'title': 'My Store - Главная'
    }


@login_required
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = product_item.name
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = OwnerProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = FullProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def test_func(self):
        self.user = self.request.user
        self.instance: Product = self.get_object()
        custom_perms = ('catalog.set_published', 'catalog.change_product_description', 'catalog.change_category')

        if self.user == self.instance.owner:
            return True
        elif self.user.groups.filter(name='moderators') and self.user.has_perms(custom_perms):
            return True
        elif self.user.is_superuser:
            return True
        return self.handle_no_permission()

    def get_form_class(self):
        if (self.object.owner == self.request.user and self.user.is_staff) or self.user.is_superuser:
            return FullProductForm
        elif self.object.owner == self.request.user:
            return OwnerProductForm
        else:
            return ModeratorProductForm


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')

    def test_func(self):
        return self.request.user.is_superuser


@user_passes_test(lambda u: u.is_staff)
def toggle_publication(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_published:
        product_item.is_published = False
    else:
        product_item.is_published = True
    product_item.save()
    return redirect(reverse('catalog:index'))
