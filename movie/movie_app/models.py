from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, FileExtensionValidator  # https://docs.djangoproject.com/en/4.0/ref/validators/#maxvaluevalidator
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User


class Director(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.full_name


class Artist(models.Model):
    full_name = models.CharField(max_length=100)
    year = models.DateField()

    def __str__(self):
        return '_'.join(self.full_name.split())


class Genre(models.Model):
    name = models.CharField(max_length=30, null=False, default='Жанр')

    def __str__(self):
        return self.name


class Movie(models.Model):
    EUR = '$'
    USD = '€'
    RUB = '₽'
    CURRENCY_CHOICES = [        # Поле Choices Field выбор из множества
        (EUR, '$'),
        (USD, '€'),
        (RUB, '₽'),
    ]

    name = models.CharField(blank=True, max_length=200) # blank можно ли оставлять пустное значение
    rating = models.IntegerField(null=False, validators=[MinValueValidator(1),
                                                         MaxValueValidator(100)])
    budged = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='R')
    year = models.DateField(null=True)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, related_name='director') # related_name - меняет обращение к внутренней таблицы
    artist = models.ManyToManyField(Artist, related_name='artist')
    genre = models.ManyToManyField(Genre, related_name='genre') # related_name Имя, которое будет использоваться для связи от связанного объекта обратно к этому
    image = models.FileField(upload_to='movie_image/', blank=' ')
    trailer = EmbedVideoField()

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name) # возвращает строку разделенную через тире
    #     super().save(*args, **kwargs)


    def get_url(self):
        return reverse('movie-detail', args=(self.slug,)) # перевод в path() используется в html

    def currency_unicode(self):
        if self.currency == 'USD':
            return "${:,}".format(self.budged)
        elif self.currency == 'EUR':
            return "€{:,}".format(self.budged)
        else:
            return "₽{:,}".format(self.budged)

    def __str__(self):
        return f'{self.name}'


class FeedBack(models.Model):
    user = models.ForeignKey(User, related_name='user_feedback', on_delete=models.CASCADE, null=True )
    feedback = models.TextField(validators=[MinLengthValidator(10)])
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    movie = models.ForeignKey(Movie, related_name='movie_feedback', on_delete=models.CASCADE, null=True, db_index=True)
    date = models.DateTimeField(auto_now_add=True)