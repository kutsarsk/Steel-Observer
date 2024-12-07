from django.urls import path, include

from Steel_Observer.events import views


urlpatterns = [
    path('', views.EventListView.as_view(), name='event-list'),
    path('create/', views.EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/', include([
        path('', views.EventDetailsView.as_view(), name='event-details'),
        path('edit/', views.EventEditView.as_view(), name='event-edit'),
        path('delete/', views.EventDeleteView.as_view(), name='event-delete'),
    ]))
]
