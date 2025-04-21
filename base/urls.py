# base/urls.py

from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('opd/', views.OPDListView.as_view(), name='list'),
    path('opd/tambah/', views.OPDCreateView.as_view(), name='create'),
    path('opd/<int:pk>/ubah/', views.OPDUpdateView.as_view(), name='update'),
    path('opd/<int:pk>/hapus/', views.OPDDeleteView.as_view(), name='delete'),
]
