from django.shortcuts import render
from articles.models import Article
# Create your views here.
def article_types(request, type_article):
    domain = Article.DOMAIN
    for j in domain:
        if j[1] == type_article:
            i = j[0]
    education = Article.objects.filter(domain = i)
    return render(request,'articles/education.html',{'education':education})

def article(request, art_id):
    article = Article.objects.get(id = art_id)
    return render(request,'articles/article.html', {'article':article})
