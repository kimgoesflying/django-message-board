from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'category', 'title',  'text')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'author': ('Автор'),
            'category': ('Категория'),
            'title': ('Заголовок'),
            'text': ('Текст'),
        }
