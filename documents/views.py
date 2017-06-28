from django.shortcuts import render
from documents.models import Document

def documents(request):
    document_type = Document.DOCUMENT_TYPES
    documents = []
    for item in document_type:
        doc = Document.objects.filter(document_type = item[0])
        documents.append({item[1]:doc})
    return render(request, "documents/documents.html", {'documents':documents})

def document(request, doc_id):
    document = Document.objects.get(id = doc_id)
    return render(request, "documents/document.html", {'document':document})
