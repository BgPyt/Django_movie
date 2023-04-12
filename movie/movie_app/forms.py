from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField, CaptchaTextInput
from .models import FeedBack
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', min_length=5)
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 5}), max_length=150)
#     rating = forms.IntegerField(label='Рейтинг', min_value=0, max_value=100)

# на основании модели FeedBack
class FeedbackForm(forms.Form):
    feedback = forms.CharField(label='Отзыв', validators=[MinLengthValidator(10)], widget=forms.Textarea(attrs={'class': 'feedback_input', 'style': 'resize: none', 'cols': 70, 'rows': 30, 'placeholder': 'comment'}))
    rating = forms.IntegerField(label='Рейтинг', validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.NumberInput(attrs={'class': 'feedback_input', 'placeholder': 'rating'}))



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input-line full-width', 'placeholder': 'username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input-line full-width', 'placeholder': '...'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input-line full-width', 'placeholder': 'password'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input-line full-width', 'placeholder': 'try password'}))
    captcha = CaptchaField(label='Капча', widget=CaptchaTextInput(attrs={'class': 'input-line full-width', 'placeholder': 'captcha'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')






class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input-line full-width', 'placeholder': 'username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input-line full-width', 'placeholder': 'password'}))
    captcha = CaptchaField(label='Капча', widget=CaptchaTextInput(attrs={'class': 'input-line full-width', 'placeholder': 'captcha'}))



