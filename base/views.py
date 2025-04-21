from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView
from .models import OPD
from .tables import OPDTable
from .forms import OPDForm

class OPDListView(SingleTableView):
    model = OPD
    table_class = OPDTable
    template_name = 'base/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Daftar OPD"
        return context


class HTMXFormMixin:
    """Mixin untuk handle HTMX form rendering dan validasi"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['action_url'] = self.request.path
        return context

    def form_valid(self, form):
        self.object = form.save()
        if self.request.headers.get('HX-Request'):
            # return JsonResponse({'success': True})
            return JsonResponse({}, status=204, headers={"HX-Trigger": "confirm_modal"})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            context = self.get_context_data(form=form)
            html = render_to_string(self.template_name, context, request=self.request)
            return JsonResponse({'html': html}, status=400)
        return super().form_invalid(form)


class OPDCreateView(HTMXFormMixin, CreateView):
    model = OPD
    form_class = OPDForm  # Gunakan OPDForm
    template_name = 'base/modal.html'
    success_url = reverse_lazy('base:list')
    title = "Tambah OPD"

class OPDUpdateView(HTMXFormMixin, UpdateView):
    model = OPD
    fields = ['kode_opd', 'nama_opd']
    template_name = 'base/modal.html'
    success_url = reverse_lazy('base:list')
    title = "Edit OPD"


class OPDDeleteView(DeleteView):
    model = OPD
    template_name = 'base/opd_confirm_delete_modal.html'
    success_url = reverse_lazy('base:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        if self.request.headers.get('HX-Request'):
            return JsonResponse({'success': True})
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Hapus OPD"
        context['action_url'] = self.request.path
        return context
