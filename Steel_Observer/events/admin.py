from django.contrib import admin

from Steel_Observer.events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'place', 'user')
    list_filter = ('name', 'date', 'place', 'user')
    search_fields = ('name', 'date', 'place', 'description', 'user')

