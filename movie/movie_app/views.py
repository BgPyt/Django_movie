from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import permissions
from .models import Movie, Artist, FeedBack, Genre
from .forms import FeedbackForm, RegisterUserForm, LoginUserForm
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, FormView, UpdateView, CreateView
from .utils import DataMixin
from math import ceil
from rest_framework import generics
from .serializers import MovieSerializer
from django.urls import reverse_lazy
from captcha.fields import CaptchaField



class MovieViews(DataMixin, ListView):
    '''FormView для отображения форм(но для сохр form_valid) и CreateView без переоределения form_valid'''
    paginate_by = 8
    model = Movie
    template_name = 'movie_app/all_movies.html'
    context_object_name = 'movies'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.user_get_context()
        context['last_page'] = ceil(len(self.model.objects.all()) / self.paginate_by)
        return dict(list(context.items()) + list(c_def.items()))


class OneMovieViews(DataMixin, DetailView): # DetailView для отображения одного экземляра модели
    template_name = 'movie_app/one_movies.html'
    model = Movie # Movie идет в шаблон в нижнем регистре
    context_object_name = 'movie' # переопредяем имя переменной в шаблоне



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = FeedBack.objects.filter(movie=kwargs['object'].id).order_by('-date')
        c_def = self.user_get_context()
        return dict(list(context.items()) + list(c_def.items()))


        


class OneArtistViews(DataMixin, TemplateView):
    template_name = 'movie_app/artist.html'

    def get_context_data(self, **kwargs):
        artist = get_object_or_404(Artist, id=kwargs['artist']) # находит экземпляр модели Artist
        context = super().get_context_data()
        context['artist'] = artist # доавляет context, для использования в шаблоне
        return context


class CommentViews(UpdateView):
    '''UpdateView для обновления уже созданной формы'''
    form_class = FeedbackForm
    model = FeedBack
    template_name = 'movie_app/edit_comment.html'
    context_object_name = 'form'
    success_url = '/'



class RegisterViews(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'movie_app/register.html'
    success_url = reverse_lazy('login-detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.user_get_context()
        return dict(list(context.items()) + list(c_def.items()))




class FilterGenreViews(DataMixin, ListView):
    template_name = 'movie_app/filtergenre.html'
    paginate_by = 8
    context_object_name = 'movies'



    def get_queryset(self):
        genre = Genre.objects.filter(name=self.kwargs['filter'])[0]
        queryset = genre.genre.distinct()
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.kwargs['filter']
        c_def = self.user_get_context()
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'movie_app/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.user_get_context()
        return dict(list(context.items()) + list(c_def.items()))


class FeedbackMovie(LoginRequiredMixin, DataMixin, FormView):
    form_class = FeedbackForm
    template_name = 'movie_app/feedback_movie.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.user_get_context()
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        movie = Movie.objects.get(id=self.kwargs['id'])
        FeedBack(user=self.request.user, feedback=form.cleaned_data['feedback'], rating=form.cleaned_data['rating'], movie=movie).save()
        return redirect('movie-detail', movie.slug)


    # def get_success_url(self): # переход на url в случае успешной входа
    #     return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')


class SearchViews(DataMixin, ListView):
    template_name = 'movie_app/all_movies.html'
    paginate_by = 2
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.filter(name__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.user_get_context()
        context['search'] = self.request.GET.get('search')
        context['last_page'] = ceil(len(self.object_list) / self.paginate_by)
        return dict(list(context.items()) + list(c_def.items()))


class MovieAPIViewsSET(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin ,GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )



