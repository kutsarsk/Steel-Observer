from django.urls import path, include

from Steel_Observer.records import views


urlpatterns = [
    path('', views.RecordListView.as_view(), name='record-list'),
    path('create/', views.RecordCreateView.as_view(), name='record-create'),
    path('<int:pk>/', include([
        path('', views.RecordDetailsView.as_view(), name='record-details'),
        path('edit/', views.RecordEditView.as_view(), name='record-edit'),
        path('delete/', views.RecordDeleteView.as_view(), name='record-delete'),
    ]))
]
