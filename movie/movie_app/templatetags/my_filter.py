from django import template
from django.template.defaultfilters import stringfilter # проверка валидности на строчный объект, иначе будет ошибка


register = template.Library() # при помощи переменной регистрировать новые фильтры

@register.filter(name='str_url') # если не установить имя, оно возмется из функции
@stringfilter
def str_url(value, key=','): # чтобы добавить фильтр в html нужно прописать {% load my_filter %} { ..|split:'передача агрумента'}
    return ', '.join(value).split()


@register.filter()
def float_rating(value:int, key=''):
    if value > 10 and value < 100:
        return '.'.join(str(value))
    elif value < 10:
        return f'0.{value}'
    else:
        return '10.0'
