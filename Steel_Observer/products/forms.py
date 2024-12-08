from django import forms

from Steel_Observer.products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product name'}),
            'description': forms.TextInput(attrs={'placeholder': 'More details'}),
        }


class ProductCreateForm(ProductForm):
    pass


class ProductEditForm(ProductForm):
    pass


class ProductDeleteForm(ProductForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
