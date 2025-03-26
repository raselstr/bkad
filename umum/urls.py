from django.urls import path
from .views import edit_group_permissions, group_list

urlpatterns = [
    path('groups/', group_list, name='group_list'),
    path('group/<int:group_id>/edit/', edit_group_permissions, name='edit_group_permissions'),
]
