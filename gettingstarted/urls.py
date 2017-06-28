from django.conf.urls import url
from django.contrib import admin
from gettingstarted import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from documents import urls
from main import urls
from news import urls
from articles import urls
from gettingstarted.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^documents/', include('documents.urls')),
    url(r'^', include('main.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
