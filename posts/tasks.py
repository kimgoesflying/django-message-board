from celery import shared_task
from .models import Reply, Post
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from datetime import datetime, timedelta
from django.contrib.auth.models import User


@shared_task
def send_mail_post_reply_task(id):
    reply = Reply.objects.get(pk=id)
    recipient = reply.post.author.email

    print(recipient)

    html_content = render_to_string(
        'posts/email/mail_post_reply.html',
        {
            'reply': reply,
            'post': reply.post,
            'url': f'http://127.0.0.1:8000/post/{reply.post.id}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'Доска объфвлений - новый отклик',
        to=[recipient],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('mail sent to', recipient)


@shared_task
def send_mail_accept_reply_task(id):
    reply = Reply.objects.get(pk=id)
    recipient = reply.author.email

    print(recipient)

    html_content = render_to_string(
        'posts/email/mail_accept_reply.html',
        {
            'reply': reply,
            'post': reply.post,
            'url': f'http://127.0.0.1:8000/post/{reply.post.id}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'Доска объявлений - отклик принят.',
        to=[recipient],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('mail sent to', recipient)


@shared_task
def posts_daily_mail_task():
    one_day_ago = datetime.today() - timedelta(days=1)
    new_posts = Post.objects.filter(date__gte=one_day_ago)
    users = User.objects.filter(groups__name='common')

    if new_posts:
        for user in users:

            html_content = render_to_string(
                'posts/email/mail_new_posts_list.html',
                {
                    'new_posts': new_posts,
                    'username': user.username,
                }
            )

            msg = EmailMultiAlternatives(
                subject='MessageBoard weekly',
                to=[user.email],
            )

            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print('--------', 'mail sent to', user.email)
