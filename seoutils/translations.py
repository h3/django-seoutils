from modeltranslation.translator import translator, TranslationOptions
from seoutils.models import Meta

class MetaTranslationOptions(TranslationOptions):
    fields = ('title', 'keywords', 'desc')
translator.register(Meta, MetaTranslationOptions)
