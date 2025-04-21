from django import forms
from .models import OPD

class OPDForm(forms.ModelForm):
    class Meta:
        model = OPD
        fields = ['kode_opd', 'nama_opd']
        widgets = {
            'kode_opd': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_opd': forms.TextInput(attrs={'class': 'form-control'}),
        }
