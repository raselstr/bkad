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

    # Buat kolom untuk tabel dari DataFrame
    columns = {col: tables.Column(verbose_name=col) for col in df.columns}

    # Buat class tabel secara dinamis
    ExcelTable = type('ExcelTable', (tables.Table,), {
        **columns,
        'Meta': type('Meta', (), {'attrs': {'class': 'table table-bordered table-striped'}})
    })

    # Buat instance tabel dengan data
    table = ExcelTable(df.to_dict(orient='records'))
    # RequestConfig(request).configure(table) # Uncomment if you want to enable pagination and sorting

    return render(request, 'dokumen/excel_table.html', {
        'table': table,
        'page_title': 'Tabel Excel'
    })