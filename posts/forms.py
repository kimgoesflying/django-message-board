from django import forms
from .models import Post
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'category', 'title',  'text')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': CKEditorWidget(),
        }

        labels = {
            'author': ('Автор'),
            'category': ('Категория'),
            'title': ('Заголовок'),
            'text': ('Текст'),
        }
