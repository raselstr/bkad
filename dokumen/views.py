import pandas as pd
import django_tables2 as tables
from django.shortcuts import render
from .search import DocumentDocument
from django.shortcuts import render
from django_tables2 import RequestConfig

def search_view(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        search = DocumentDocument.search().query(
            "multi_match",
            query=query,
            fields=['title', 'content']
        )
        response = search.execute()
        results = response.hits

    return render(request, 'dokumen/search_results.html', {'results': results, 'query': query})




def excel_table_view(request):
    df = pd.read_excel('D:/Cloud/2025/REALISASI 2025/Realisasi/06 Juni.xlsx')

    # Buat table class dinamis dari kolom-kolom di DataFrame
    class ExcelTable(tables.Table):
        class Meta:
            attrs = {"class": "table table-bordered table-striped"}

    for col in df.columns:
        ExcelTable.base_columns[col] = tables.Column(verbose_name=col)

    table = ExcelTable(df.to_dict(orient='records'))

    return render(request, 'dokumen/excel_table.html', {
        'table': table
    })