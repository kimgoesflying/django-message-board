from django_filters import FilterSet, DateFilter, DateRangeFilter, ModelMultipleChoiceFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):

    # start_date = DateFilter(field_name='date', lookup_expr=(
    #     'gt'), widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}), label='от')

    # end_date = DateFilter(field_name='date', lookup_expr=(
    #     'lt'), widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}), label='до')

    # date = DateRangeFilter(label='Дата', widget=forms.Select(
    #     attrs={'class': 'form-control'}))

    # category = ModelMultipleChoiceFilter(queryset=Post.objects.all(),
    #                                      widget=forms.CheckboxSelectMultiple(),  label='Категории')

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
