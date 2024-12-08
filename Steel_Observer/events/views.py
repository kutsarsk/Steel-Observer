from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from Steel_Observer.events.forms import EventCreateForm, EventEditForm, EventDeleteForm
from Steel_Observer.events.models import Event
from Steel_Observer.permissions import PermissionMixin


class EventCreateView(LoginRequiredMixin, CreateView):

    model = Event
    form_class = EventCreateForm
    template_name = 'events/event-create.html'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user

        if not form.is_valid():
            print(form.errors)

        event.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('event-details', kwargs={'pk': self.object.pk})


class EventDetailsView(DetailView):

    model = Event
    template_name = 'events/event-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_created_event'] = self.get_object().user == self.request.user
        return context


class EventEditView(LoginRequiredMixin, PermissionMixin, UpdateView):

    model = Event
    form_class = EventEditForm
    template_name = 'events/event-edit.html'

    def get_success_url(self):
        return reverse_lazy('event-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_created_event'] = self.get_object().user == self.request.user
        return context


class EventDeleteView(LoginRequiredMixin, PermissionMixin, DeleteView):

    model = Event
    template_name = 'events/event-delete.html'
    form_class = EventDeleteForm

    def get_initial(self):
        obj = self.get_object()
        return {'name': obj.name, 'date': obj.date, 'place': obj.place, 'description': obj.description}

    def get_success_url(self):
        return reverse_lazy('event-list')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for field in form.fields.values():
            field.disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_created_event'] = self.get_object().user == self.request.user
        return context


class EventListView(ListView):

    model = Event
    template_name = 'events/event-list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['events'] = Event.objects.all().order_by('-date', 'name', 'place', 'pk')
        return context
