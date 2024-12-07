from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from Steel_Observer.events.forms import EventCreateForm, EventEditForm, EventDeleteForm
from Steel_Observer.events.models import Event


class EventCreateView(LoginRequiredMixin, CreateView):

    model = Event
    form_class = EventCreateForm
    template_name = 'events/event-create.html'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('event-details', kwargs={'pk': self.request.user.pk})


class EventDetailsView(DetailView):

    model = Event
    template_name = 'events/event-details.html'


class EventEditView(LoginRequiredMixin, UpdateView):

    model = Event
    form_class = EventEditForm
    template_name = 'events/event-edit.html'

    def user_created_event(self):
        event = get_object_or_404(Event, user=self.request.user)
        return self.request.user == event.user

    def get_success_url(self):
        return reverse_lazy('event-details', kwargs={'user_pk': self.request.user.pk})


class EventDeleteView(LoginRequiredMixin, DeleteView):

    model = Event
    template_name = 'events/event-delete.html'
    form_class = EventDeleteForm

    def get_success_url(self):
        return reverse_lazy('home')

    def user_created_event(self):
        event = get_object_or_404(Event, user=self.request.user)
        return self.request.user == event.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'data': self.get_initial()})
        return kwargs


class EventListView(ListView):

    model = Event
    template_name = 'events/event-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['events'] = Event.objects.all().order_by('-date', 'name', 'place', 'pk')
        return context

    paginate_by = 20