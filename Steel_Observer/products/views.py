from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from Steel_Observer.permissions import PermissionMixin
from Steel_Observer.products.forms import ProductCreateForm, ProductEditForm, ProductDeleteForm
from Steel_Observer.products.models import Product


class ProductCreateView(LoginRequiredMixin, CreateView):

    model = Product
    form_class = ProductCreateForm
    template_name = 'products/product-create.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user

        if not form.is_valid():
            print(form.errors)

        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product-details', kwargs={'pk': self.object.pk})


class ProductDetailsView(DetailView):

    model = Product
    template_name = 'products/product-details.html'
    context_object_name = 'product'
    paginate_by = 10

    def get_related_records(self):
        product = self.get_object()
        return product.record_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['product'] = self.get_object()
        related_records = self.get_related_records().order_by('-date', 'region', 'type', 'pk')
        paginator = Paginator(related_records, self.paginate_by)
        page = self.request.GET.get('page')
        context['records'] = paginator.get_page(page)
        context['record_count'] = related_records.count()
        context['user_created_product'] = self.get_object().user == self.request.user
        return context


class ProductEditView(LoginRequiredMixin, PermissionMixin, UpdateView):

    model = Product
    form_class = ProductEditForm
    template_name = 'products/product-edit.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user

        if not form.is_valid():
            print(form.errors)

        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product-details', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_created_product'] = self.get_object().user == self.request.user
        return context


class ProductDeleteView(LoginRequiredMixin, PermissionMixin, DeleteView):

    model = Product
    template_name = 'products/product-delete.html'
    form_class = ProductDeleteForm

    def get_success_url(self):
        return reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'data': self.get_initial()})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_created_product'] = self.get_object().user == self.request.user
        return context


class ProductListView(ListView):

    model = Product
    template_name = 'products/product-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        all_products = Product.objects.all().order_by('name')
        paginator = Paginator(all_products, self.paginate_by)
        page = self.request.GET.get('page')
        context['products'] = paginator.get_page(page)
        context['product_count'] = all_products.count()
        return context
