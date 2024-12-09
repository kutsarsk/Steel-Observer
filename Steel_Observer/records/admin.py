from django.contrib import admin

from Steel_Observer.records.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'region', 'product', 'quantity', 'currency', 'price', 'type', 'user')
    list_filter = ('date', 'region', 'product', 'quantity', 'currency', 'price', 'type', 'user')
    search_fields = ('date', 'region', 'product', 'quantity', 'currency', 'price', 'type', 'user')
