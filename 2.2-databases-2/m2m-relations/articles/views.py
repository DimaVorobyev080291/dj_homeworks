from django.shortcuts import render
from django.db.models import Prefetch
from articles.models import Article , ArticleThema


def articles_list(request):
    """
    Функция передает в браузер на страницу news.html словарь context со статьями
    В словарь помещаем статьи отсортированные по дате в порядке убывания со связанными с ними темами
    """
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {
        'object_list': Article.objects.order_by(ordering).prefetch_related(
            Prefetch('themas', queryset=ArticleThema.objects.select_related('thema')))
    }

    return render(request, template, context)
