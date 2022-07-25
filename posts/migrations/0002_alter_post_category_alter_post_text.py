# Generated by Django 4.0.6 on 2022-07-25 19:30

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('tnk', 'Танки'), ('hlr', 'Хилы'), ('dd', 'ДД'), ('trd', 'Торговцы'), ('gm', 'Гилдмастеры'), ('qg', 'Квестгиверы'), ('blksm', 'Кузнецы'), ('lthwrk', 'Кожевники'), ('pm', 'Зельевары'), ('sm', 'Мастера заклинаний')], default='tnk', max_length=6),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
