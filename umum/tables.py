import django_tables2 as tables
from django.contrib.auth.models import Group

class GroupTable(tables.Table):
    id = tables.Column(verbose_name="ID", orderable=False, attrs={"td": {"class": "text-center"}})
    edit = tables.TemplateColumn(
        '<a href="{% url \'umum:edit\' record.id %}" class="btn btn-warning btn-sm">'
        '<i class="ti ti-edit"></i> Edit</a>',
        orderable=False,
        verbose_name="Actions",
        attrs={"td": {"class": "text-center"}},
    )
    
    class Meta:
        model = Group
        template_name = "django_tables2/bootstrap5.html"
        fields = ("id", "name")
        attrs = {
            "class": "table table-sm table-striped table-bordered table-hover table-responsive",
            "thead": {"class": "table-dark"},
            "th": {"class": "text-center"},
            }
        
        