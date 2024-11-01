from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, Thema, ArticleThema
from django.forms import BaseInlineFormSet


class ArticleThemaInlineFormset(BaseInlineFormSet):
    """
    Если данные не заполнены или оснавных тем 2 или больше, то не сохраняем данные 
    и сообщаем пользователю об ошибке.
    Если основная тема не указана сообщаем пользователю о необходимости выбрать одну основную тему
    """
    def clean(self):
        is_main = False
        for form in self.forms:
            form.cleaned_data
            
            if form.cleaned_data.get('is_main'):
                if not is_main:
                    is_main = True
                else:
                    raise ValidationError('Основная тема возможна только одна.')

            if not is_main:
                raise ValidationError('Укажите основной раздел')
        return super().clean() 



class ArticleThemaInline(admin.TabularInline):
    """
    InLine сущьность связи моделей 
    """
    model = ArticleThema
    formset = ArticleThemaInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Админка модели Article
    """
    list_display = ['id','title', 'summary', 'published_at', 'image']
    inlines = [ArticleThemaInline]

    @admin.display(description="Text")
    def summary(self, obj) -> str:
        """
        Метод конвертации столбца 'text' в короткую запись
        """
        if len(obj.text)> 30:
            return f"{obj.text[:20]}..."
        return obj.text
            

@admin.register(Thema)
class ThemaAdmin(admin.ModelAdmin):
    """
    Админка модели Thema
    """
    list_display = ['id', 'thema']
    inlines = [ArticleThemaInline]

@admin.register(ArticleThema)
class ArticleThemaAdmin(admin.ModelAdmin):
    """    
    Админка модели ArticleThema
    """
    list_display = ['id', 'article', 'thema', 'is_main']