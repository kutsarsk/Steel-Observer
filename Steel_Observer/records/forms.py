from django import forms

from Steel_Observer.products.models import Product
from Steel_Observer.records.models import Record


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        exclude = ['user']
        labels = {
            'product': 'Type of product:',
            'quantity': 'Quantity (metric tons):',
            'price': 'Price per metric ton:',
            'type': 'Type of transaction'
        }

    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label='Select a product')


class RecordCreateForm(RecordForm):
    pass


class RecordEditForm(RecordForm):
    pass


class RecordDeleteForm(RecordForm):
    pass
