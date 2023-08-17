from django.forms import ModelForm, forms
from .models import Post
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'post_type', 'title', 'text']
        widgets = {
            'author': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите имя автора'
            }),
            'post_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите тип статьи'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название статьи'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст статьи'
            }),
        }
