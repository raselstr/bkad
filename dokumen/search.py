from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from .models import Document as DocumentModel

document_index = Index('documents')

@registry.register_document
class DocumentDocument(Document):
    class Index:
        name = 'documents'

    class Django:
        model = DocumentModel
        fields = [
            'title',
            'content',
        ]
