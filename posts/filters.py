from django_filters import FilterSet, BooleanFilter
from .models import Post, Reply
from django import forms


class PostFilter(FilterSet):
    class Meta:
        model = Post

        fields = [
            'category',
        ]

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['category'].label = ""
        self.filters['category'].field.widget.attrs.update(
            {'class': 'form-control'})


class ReplyFilter(FilterSet):
    answerd = BooleanFilter(field_name='status', label='Принято')

    class Meta:
        model = Reply

        fields = [
            'post',
            'answerd'
        ]

    def __init__(self, *args, **kwargs):
        super(ReplyFilter, self).__init__(*args, **kwargs)
        self.filters['post'].field.widget.attrs.update(
            {'class': 'form-control'})
        self.filters['answerd'].field.widget.attrs.update(
            {'class': 'form-control'})
