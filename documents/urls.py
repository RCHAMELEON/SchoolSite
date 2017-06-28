from django.conf.urls import url
from documents import views
from documents.documentviews import DocumentCreate

urlpatterns = [
    url(r'^list/$', views.documents, name='list'),
    url(r'^document/(?P<doc_id>\d+)/$', views.document, name="document"),
    url(r'^adddocument/$', DocumentCreate.as_view(), name="adddocument"),
]
