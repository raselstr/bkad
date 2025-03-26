from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group
from .forms import GroupPermissionForm

def edit_group_permissions(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == "POST":
        form = GroupPermissionForm(request.POST, instance=group)
        if form.is_valid():
            group.permissions.set(form.cleaned_data['permissions'])
            return redirect('group_list')  # Redirect ke daftar grup
    else:
        form = GroupPermissionForm(instance=group)

    return render(request, 'umum/edit_permissions.html', {'form': form, 'group': group})

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'umum/group_list.html', {'groups': groups})
