from django import forms
from django.contrib.auth.models import Group, Permission

class GroupPermissionForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="User Permissions"
    )

    class Meta:
        model = Group
        fields = ['permissions']
