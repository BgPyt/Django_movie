from .models import *


class DataMixin:

    def user_get_context(self, **kwargs):
        context = kwargs
        genres = Genre.objects.order_by('name')
        context['genres'] = genres
        return context
