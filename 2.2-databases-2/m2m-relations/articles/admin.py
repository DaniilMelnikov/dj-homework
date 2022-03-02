from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        list_tag = []
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data == {}:
                break
            if form.cleaned_data['tag'] in list_tag:
                raise ValidationError('Нельзя использовать повторяющиеся теги')
            else:
                list_tag.append(form.cleaned_data['tag'])
            if form.cleaned_data['is_main']:
                count += 1
            if count > 1:
                raise ValidationError('is_main может быть только одним')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            
            #raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
