import django_tables2 as tables
from django.contrib.auth.models import Group

class GroupTable(tables.Table):
    id = tables.Column(verbose_name="ID", orderable=False, attrs={"td": {"class": "text-center"}})
    actions = tables.TemplateColumn(
        template_code='''
            <a href="{% url 'umum:role' record.id %}" class="btn btn-info btn-sm me-1">
                <i class="ti ti-subtask"></i> Role
            </a>
            <a href="#"
                class="btn btn-warning btn-sm"
                hx-get="{% url 'umum:edit' record.id %}"
                hx-target="#filter .modal-content"
                hx-trigger="click"
                hx-swap="innerHTML"
                data-bs-toggle="modal"
                data-bs-target="#filter">
                <i class="ti ti-edit"></i> Edit
            </a>
            <button 
                    class="btn btn-danger btn-sm"
                    hx-get="{% url 'umum:confirm_delete' record.id %}"
                    hx-target="#modal-content"
                    hx-trigger="click"
                    hx-swap="innerHTML"
                    data-bs-toggle="modal"
                    data-bs-target="#filter">
                    <i class="ti ti-trash"></i> Delete
                </button>
        ''',
        verbose_name="Actions",
        orderable=False,
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
        
        