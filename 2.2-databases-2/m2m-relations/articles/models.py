from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Thema(models.Model):
    """
    Создаем таблицу тем Thema связанную с таблицей статей Article связью Многие-Ко-Многим
    """
    thema = models.CharField(max_length=50, verbose_name='Тема')
    articles = models.ManyToManyField(Article, through='ArticleThema')

    def __str__(self):
        return self.thema

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class ArticleThema(models.Model):
    """
    Промежуточная таблица для связи Многие-Ко-Многим между Article и Thema
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='themas')
    thema = models.ForeignKey(Thema, on_delete=models.CASCADE, verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name='Основной', blank=True)

    def __str__(self):
        return f'{self.article}_{self.thema}'

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'