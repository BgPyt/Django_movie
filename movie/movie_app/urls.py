from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', views.MovieViews.as_view(), name='home'),
    path('movie/<slug:slug>', views.OneMovieViews.as_view(), name='movie-detail'), # slug если по слагу или pk = primary_Key если по ключу (id)
    path('artist/<int:artist>', views.OneArtistViews.as_view(), name='artist-detail'),
    path('comment/<int:pk>', views.CommentViews.as_view(), name='comment-detail'),
    path('login', views.LoginUser.as_view(), name='login-detail'),
    path('register', views.RegisterViews.as_view(), name='register-detail'),
    path('movie/<filter>', views.FilterGenreViews.as_view(), name='filter-detail'),
    path('exit', views.logout_user, name='logout'),
    path('movie/review/<int:id>', views.FeedbackMovie.as_view(), name='review-detail'),
    path('search', views.SearchViews.as_view(), name='search-detail')
]