from django.shortcuts import render
from django.views.generic import ListView

from Steel_Observer.records.models import Record


class HomePageView(ListView):

    model = Record
    template_name = 'home.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['records'] = Record.objects.all().order_by('-date', 'id')
        return context
