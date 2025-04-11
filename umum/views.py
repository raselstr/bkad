from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.models import Group
from .forms import GroupPermissionForm, GroupForm
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q

from .tables import GroupTable

def role(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == "POST":
        form = GroupPermissionForm(request.POST, instance=group)
        if form.is_valid():
            group.permissions.set(form.cleaned_data['permissions'])
            return redirect('umum:list')  # Redirect ke daftar grup
    else:
        form = GroupPermissionForm(instance=group)
    
    context = {
        'form': form,
        'group': group,
        'title': 'Edit Permissions for Group'
    }
    return render(request, 'umum/edit_permissions.html', context)


def confirm(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request, 'umum/confirm.html', {
        'group': group,
        'title': 'Konfirmasi Hapus'
    })

def delete(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == "POST":
        group.delete()
        return JsonResponse({}, status=204, headers={"HX-Trigger": "confirm_modal"})

def edit(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)  # <-- PENTING: instance=group
        if form.is_valid():
            form.save()
            return JsonResponse({}, status=204, headers={"HX-Trigger": "confirm_modal"})
        else:
            # Form tidak valid, render ulang modal dengan error
            return render(request, 'umum/modal.html', {
                'form': form,
                'title': 'Edit Group',
                'action_url': reverse('umum:edit', args=[group.id])
            })

    # GET: tampilkan form edit di modal
    form = GroupForm(instance=group)
    return render(request, 'umum/modal.html', {
        'form': form,
        'title': 'Edit Group',
        'action_url': reverse('umum:edit', args=[group.id])
    })

def add(request):
    form = GroupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return JsonResponse({}, status=204, headers={"HX-Trigger": "confirm_modal"})
        else:
            # ❗ JANGAN return layout lengkap
            return render(request, 'umum/modal.html', {
                'form': form,
                'title': 'Add Group',
            })

    return render(request, 'umum/group_list.html', {
        'form': form,
        'title': 'Add Group',
        'action_url': reverse('umum:add')
    })

def modal(request):
    form = GroupForm(request.GET or None)
    context = {
        'form': form,
        'title': 'Add Group',
        'action_url': reverse('umum:add')
    }
    return render(request, 'umum/modal.html', context)

def list(request):
    queryset = Group.objects.all().order_by('id')
    table = GroupTable(queryset)  # TANPA table.paginate()

    context = {
        'table': table,
        'title': 'Group List',
        'url_add': reverse('umum:add'),
        'url_modal': reverse('umum:modal'),
    }
    return render(request, 'umum/group_list.html', context)

# def list(request):
#     table = GroupTable(Group.objects.all().order_by('id'))
#     table.paginate(page=request.GET.get("page", 1), per_page=10)
#     form = GroupForm(request.GET or None)
#     context = {
#         'table': table,
#         'form': form,
#         'title': 'Group List',
#         'url_add': reverse('umum:add'),
#         'url_modal' : reverse('umum:modal')
#     }
#     return render(request, 'umum/group_list.html', context)

# def list(request):
#     search_query = request.GET.get('search', '')
#     per_page = request.GET.get('per_page', '10')

#     if per_page == 'all':
#         per_page = None
#     else:
#         try:
#             per_page = int(per_page)
#         except ValueError:
#             per_page = 10

#     queryset = Group.objects.all().order_by('id')
#     if search_query:
#         queryset = queryset.filter(
#             Q(name__icontains=search_query)
#             # Q(description__icontains=search_query)
#         )

#     table = GroupTable(queryset)
#     if per_page:
#         table.paginate(page=request.GET.get("page", 1), per_page=per_page)

#     context = {
#         'table': table,
#         'search_query': search_query,
#         'per_page': request.GET.get('per_page', '10'),
#     }

#     if request.htmx:
#         html = render_to_string('umum/partials/group_table_partial.html', context, request=request)
#         return HttpResponse(html)

#     # Full page render
#     context.update({
#         'form': GroupForm(request.GET or None),
#         'title': 'Group List',
#         'url_add': reverse('umum:add'),
#         'url_modal': reverse('umum:modal'),
#     })
#     return render(request, 'umum/group_list.html', context)
    

