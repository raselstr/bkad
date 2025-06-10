from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('excel/', views.excel_table_view, name='excel_table'),
]
