from django.urls import path
from . import views

app_name = 'umum'
urlpatterns = [
    path('groups/filter/', views.filter, name='filter'),
    path('groups/add/', views.group_add, name='add'),
    path('groups/', views.group_list, name='list'),
    path('group/<int:group_id>/edit/', views.edit, name='edit'),
]
