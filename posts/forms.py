from django import forms
from .models import Post, Reply
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('category', 'title',
                  'featured_image', 'featured_text', 'text')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_text': forms.Textarea(attrs={'class': 'form-control', 'style': "height: 80px"}),
            'text': CKEditorWidget(),
        }

        labels = {
            'category': ('Категория'),
            'title': ('Заголовок'),
            'featured_image': ('картинка'),
            'featured_text': ('короткий текст'),
            'text': ('Текст'),
        }


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'style': "height: 80px"}),
        }

        labels = {
            'text': ('Текст'),
        }
