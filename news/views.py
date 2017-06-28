from django.shortcuts import render
from news.models import New
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator

def news(request,page=1):
    news = New.objects.all()
    paginator = Paginator(news, 4)
    news = {'news': paginator.page(page), }
    return render(request, 'news/news.html', news)

def new(request, new_id):
    new = New.objects.get(id=new_id)
    return render(request, 'news/new.html', {'new':new})

def addlike(request, new_id):
    user = str(request.user) + str(new_id)
    try:
        if user in request.COOKIES:
            return redirect("/news/new/"+new_id)
        else:
            new = New.objects.get(id=new_id)
            new.like += 1
            new.save()
            response = redirect("/news/new/"+new_id)
            response.set_cookie(user, "addLike")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect("/")
