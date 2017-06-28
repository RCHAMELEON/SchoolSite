from django.shortcuts import render
from news.models import New
from articles.models import Article
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.
def index(request):
    result = New.objects.all()
    nws = [result[(len(result) - 2)], result[(len(result) - 1)]]
    psy = Article.objects.filter(domain = 'PSY')
    return render(request, 'main/index.html', {"lastnews":nws, "physical":psy})

def admin(request):
    return render(request, 'bar.html')

def register(request):
    args = {}
    args["form"] = UserCreationForm

    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid:
            user_form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('/')
    return render(request, 'register.html', args)
