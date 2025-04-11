from django.urls import path
from . import views

app_name = 'umum'
urlpatterns = [
    path('groups/filter/', views.filter, name='filter'),
    path('groups/add/', views.add, name='add'),
    path('groups/', views.list, name='list'),
    path('group/<int:group_id>/role/', views.role, name='role'),
    path('group/<int:group_id>/edit/', views.edit, name='edit'),
    path('group/<int:group_id>/delete/', views.delete, name='delete'),
    path('group/<int:group_id>/confirm/', views.confirm, name='confirm_delete'),
]
