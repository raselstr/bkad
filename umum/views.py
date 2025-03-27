from django.shortcuts import render, get_object_or_404, redirect
from django_tables2 import RequestConfig, SingleTableView
from django.urls import reverse
from django.contrib.auth.models import Group
from .forms import GroupPermissionForm, GroupForm

from .tables import GroupTable



def edit(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == "POST":
        form = GroupPermissionForm(request.POST, instance=group)
        if form.is_valid():
            group.permissions.set(form.cleaned_data['permissions'])
            return redirect('group_list')  # Redirect ke daftar grup
    else:
        form = GroupPermissionForm(instance=group)
    
    context = {
        'form': form,
        'group': group,
        'title': 'Edit Permissions for Group'
    }
    return render(request, 'umum/edit_permissions.html', context)


def group_list(request):
    table = GroupTable(Group.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=20)
    form = GroupForm(request.GET or None)
    context = {
        'table': table,
        'form': form,
        'title': 'Group List',
        'url_add': reverse('umum:add'),
        'url_filter' : reverse('umum:filter')
    }
    return render(request, 'umum/group_list.html', context)

def group_add(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('umum:list')  # Redirect ke daftar grup
    else:
        form = GroupForm()
    
    context = {
        'form': form,
        'title': 'Add Group',
        'url_add': reverse('umum:add')
        
    }
    return render(request, 'umum/group_add.html', context)

def filter(request):
    form = GroupForm(request.GET or None)
    context = {
        'form': form,
    }
    return render(request, 'umum/filter.html', context)
    

