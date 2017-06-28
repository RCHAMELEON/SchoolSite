from django.conf.urls import url
from articles import views
from articles.articleviews import ArticleCreate,ArticleUpdate,ArticleDelete

urlpatterns = [
    url(r'^(?P<type_article>\w+)/$', views.article_types, name='education'),
    url(r'^add', ArticleCreate.as_view(), name="addarticle"),
    url(r'^article/(?P<art_id>\d+)/$', views.article, name="article"),
    url(r'^article/(?P<art_id>\d+)/edit/$', ArticleUpdate.as_view(), name="updatearticle"),
    url(r'^article/(?P<pk>\d+)/delete/$', ArticleDelete.as_view(), name="deletearticle"),
]
