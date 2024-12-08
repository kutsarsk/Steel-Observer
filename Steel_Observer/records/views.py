from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from Steel_Observer.permissions import PermissionMixin
from Steel_Observer.records.forms import RecordCreateForm, RecordEditForm, RecordDeleteForm
from Steel_Observer.records.models import Record


class RecordCreateView(LoginRequiredMixin, CreateView):

    model = Record
    form_class = RecordCreateForm
    template_name = 'records/record-create.html'

    def form_valid(self, form):
        record = form.save(commit=False)
        record.user = self.request.user

        if not form.is_valid():
            print(form.errors)

        record.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('record-list')


class RecordDetailsView(DetailView):

    model = Record
    template_name = 'records/record-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_created_record'] = self.get_object().user == self.request.user
        return context


class RecordEditView(LoginRequiredMixin, PermissionMixin, UpdateView):
    model = Record
    form_class = RecordEditForm
    template_name = 'records/record-edit.html'

    def form_valid(self, form):
        record = form.save(commit=False)
        record.user = self.request.user

        if not form.is_valid():
            print(form.errors)

        record.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('record-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_created_record'] = self.get_object().user == self.request.user
        return context


class RecordDeleteView(LoginRequiredMixin, PermissionMixin, DeleteView):

    model = Record
    template_name = 'records/record-delete.html'
    form_class = RecordDeleteForm

    def get_success_url(self):
        return reverse_lazy('record-list')

    def get_initial(self):
        obj = self.get_object()
        return {'product': obj.product, 'quantity': obj.quantity, 'currency': obj.currency, 'price': obj.price, 'type': obj.type}

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        for field in form.fields.values():
            field.disabled = True
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_created_record'] = self.get_object().user == self.request.user
        return context


class RecordListView(ListView):

    model = Record
    template_name = 'records/record-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        all_records = Record.objects.all().order_by('-date', 'product', 'region', 'type', 'pk')
        paginator = Paginator(all_records, self.paginate_by)
        page = self.request.GET.get('page')
        context['records'] = paginator.get_page(page)
        context['record_count'] = all_records.count()
        return context


