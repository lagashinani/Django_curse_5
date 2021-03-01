from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleScope, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        for form in self.forms:

            if form.cleaned_data.get('is_main') and not form.cleaned_data.get('DELETE'):
                is_main_count += 1
            if is_main_count > 1:
                raise ValidationError('Основным может быть только один раздел')
        if is_main_count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = ArticleScope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


admin.site.register(Scope)
