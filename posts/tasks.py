from celery import shared_task
from .models import Reply
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


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
            'post_url': f'http://127.0.0.1:8000/posts/{reply.post.id}'
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
            'post_url': f'http://127.0.0.1:8000/posts/{reply.post.id}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'Доска объявлений - отклик принят.',
        to=[recipient],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('mail sent to', recipient)
