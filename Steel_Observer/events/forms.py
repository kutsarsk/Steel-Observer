from django.forms import ModelForm

from Steel_Observer.events.models import Event


class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = '__all__'


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
