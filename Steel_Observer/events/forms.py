from django import forms

from Steel_Observer.events.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'event name'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'place': forms.TextInput(attrs={'placeholder': 'event place'}),
            'description': forms.TextInput(attrs={'placeholder': 'event description'}),
        }


class EventCreateForm(EventForm):
    pass


class EventEditForm(EventForm):
    pass


class EventDeleteForm(EventForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
