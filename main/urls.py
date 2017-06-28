from django.conf.urls import url
import main.views
import django.contrib.auth.views as views

urlpatterns = [
    url(r'^$', main.views.index, name="index"),
    url(r'^login/$', views.login,{"template_name":"login.html"}, name="login"),
    url(r'^permissions/$',  main.views.admin, name = "bar"),
    url(r'^register/$', main.views.register, name = "register")
]
