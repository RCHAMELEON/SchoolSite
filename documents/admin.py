from django.contrib import admin
from documents.models import Document
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    model = Document
    fields = ["title","desctiption","document_type","fiel","tags"]
    list_display = ["title","document_type"]
    search_fields = ["title","document_type"]


admin.site.register(Document, DocumentAdmin)
