import django_tables2 as tables
from .models import OPD

class OPDTable(tables.Table):
    aksi = tables.TemplateColumn(template_name='base/columns/aksi_kolom.html', orderable=False, verbose_name='Aksi')

    class Meta:
        model = OPD
        template_name = "django_tables2/bootstrap5.html"
        fields = ('kode_opd', 'nama_opd')  # urutan kolom
