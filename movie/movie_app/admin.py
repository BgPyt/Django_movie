from django.contrib import admin, messages # messages уровни сообщения (ошибка, предупреждение и тд)
from .models import Movie, Director, Artist, Genre
from django.db.models import QuerySet, Q

# Register your models here.


class RatingFilter(admin.SimpleListFilter): # класс с фильтровкой значений
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(Q(rating__gte=40) & Q(rating__lte=59))
        if self.value() == 'от 60 до 79':
            return queryset.filter(Q(rating__gte=60) & Q(rating__lte=79))
        elif self.value() == '>=80':
            return queryset.filter(rating__gte=80)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']
    list_editable = ['email']

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'year']
    list_editable = ['year']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )} # вычисляте slug при добавлении имени
    # exclude = []  исключить добавление полей при создании новой строки
    # readonly_fields = ['year']  остается пользователем , но менять он не сможет
    list_display = ['name', 'rating', 'budged', 'year', 'director', 'rating_status']
    list_editable = ['rating', 'budged', 'year', 'director']
    ordering = ['name', 'year'] # сортировка по имени и по году
    list_per_page = 10 # пагиная отображения на одной странице элементов
    actions = ['set_dollars', 'set_euro'] # регистрация нового дейтсвия в интерфейс админа
    search_fields = ['name__istartswith'] # поиск по имени первым буквам
    list_filter = ['name', 'currency', RatingFilter]
    filter_horizontal = ['genre', 'artist']


    @admin.display(ordering='rating', description='Статус') # создать сортировку новой колонки
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Плохой фильм!'

        elif movie.rating < 60:
            return 'На один раз!'

        elif movie.rating < 75:
            return 'Неплохой'

        elif movie.rating < 90:
            return 'Потрясающий фильм!'

        elif movie.rating < 100:
            return 'Великолепно!'

    @admin.action(description='Установить валюту в доллар') # добавление нового действия
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')  # добавление нового действия
    def set_euro(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.EUR)
        self.message_user(request,
                          f'Вы обновили: {queryset.count()} значения')

# имя name в list_editable убрано, потому что должно выступать в качестве отобр изменяемой стройки
# admin.site.register(Movie, MovieAdmin)  к Movie привязывается MovieAdmin