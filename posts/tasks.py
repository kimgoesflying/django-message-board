from celery import shared_task
import time
from .models import Reply
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@shared_task
def hello():
    time.sleep(5)
    print("Hello, world!")


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
        subject=f'Message Board - отклик {reply.post.title}',
        to=[recipient],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('mail sent to', recipient)
