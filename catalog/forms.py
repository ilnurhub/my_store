from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    VALIDATION_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in self.VALIDATION_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенный продукт')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in self.VALIDATION_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError('Запрещенный продукт')
        return cleaned_data
