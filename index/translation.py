from modeltranslation.translator import translator, TranslationOptions
from .models import News, Category


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
