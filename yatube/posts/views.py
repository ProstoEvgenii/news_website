from django.shortcuts import render

from django.http import HttpResponse
from .models import Post


def index(request):
    # главная страница
    # одна строка вместо тысячи слов на SQL
    posts = Post.objects.order_by('-pub_date')
    # собираем тексты постов в один, разделяя новой строкой
    return render(request, 'posts/home.html', {'posts': posts})
    # return HttpResponse('<h1>Главная страница </h1>'+'\n'.join(output))
    # return HttpResponse("<h1>Главная страница</h1>")


def about(request):
    return render(request, 'posts/about.html')


def add_news(request):
    return render(request, 'posts/add_news.html')





# def get_group(request, slug):
    
# def test(request):
#     return HttpResponse("<h1>Кажется получается</h1>")
