# Generated by Django 4.0.6 on 2022-07-25 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
    ]