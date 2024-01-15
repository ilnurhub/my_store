from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ValidationMixin:
    VALIDATION_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

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


class FullProductForm(StyleFormMixin, ValidationMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['owner'].widget = forms.HiddenInput()


class OwnerProductForm(StyleFormMixin, ValidationMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['owner'].widget = forms.HiddenInput()
        self.fields['is_published'].widget = forms.HiddenInput()


class ModeratorProductForm(StyleFormMixin, ValidationMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('is_published', 'description', 'category')


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
