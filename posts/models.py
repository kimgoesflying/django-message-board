from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    POST_TYPE = (
        ('tnk', 'Танки'),
        ('hlr', 'Хилы'),
        ('dd', 'ДД'),
        ('trd', 'Торговцы'),
        ('gm', 'Гилдмастеры'),
        ('qg', 'Квестгиверы'),
        ('blksm', 'Кузнецы'),
        ('lthwrk', 'Кожевники'),
        ('pm', 'Зельевары'),
        ('sm', 'Мастера заклинаний'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Дата', default=timezone.now)
    category = models.CharField(max_length=6, choices=POST_TYPE, default='tnk')
    title = models.CharField(max_length=100)
    featured_image = models.ImageField(
        upload_to='featured_image/%Y/%m/%d/', blank=True, null=True)
    featured_text = models.TextField(blank=True, null=True)
    text = RichTextUploadingField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
