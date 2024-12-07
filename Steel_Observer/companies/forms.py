from django import forms

from Steel_Observer.companies.models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Company name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Company location'}),
            'products': forms.TextInput(attrs={'placeholder': 'Products traded'}),
        }


class CompanyCreateForm(CompanyForm):
    pass


class CompanyEditForm(CompanyForm):
    pass


class CompanyDeleteForm(CompanyForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
