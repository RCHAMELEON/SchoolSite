from django.conf.urls import url
from news import views
from news.newviews import NewCreate, NewUpdate, NewDelete

urlpatterns = [
    url(r'^index/$', views.news, name='news'),
    url(r'^page/(?P<page>\d+)/$', views.news, name = "page"),
    url(r'^new/(?P<new_id>\d+)/$', views.new, name="new"),
    url(r'^new/(?P<new_id>\d+)/edit/$', NewUpdate.as_view(), name="updatenew"),
    url(r'^new/(?P<pk>\d+)/delete/$', NewDelete.as_view(), name="delnew"),
    url(r'^addnew/$', NewCreate.as_view(), name = "addnew"),
    url(r'^new/addlike/(?P<new_id>\d+)/$', views.addlike, name="addlike"),
]
