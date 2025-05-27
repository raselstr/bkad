from django.shortcuts import render
from .search import DocumentDocument

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

    return render(request, 'search_results.html', {'results': results, 'query': query})
