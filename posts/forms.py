from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'category', 'title',
                  'featured_image', 'featured_text', 'text')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_text': forms.Textarea(attrs={'class': 'form-control', 'style': "height: 80px"}),
            'text': CKEditorWidget(),
        }

        labels = {
            'author': ('Автор'),
            'category': ('Категория'),
            'title': ('Заголовок'),
            'featured_image': ('картинка'),
            'featured_text': ('короткий текст'),
            'text': ('Текст'),
        }
