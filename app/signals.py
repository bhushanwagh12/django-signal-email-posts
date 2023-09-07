# models.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import Post
from .utils import send_post_created_email

@receiver(post_save, sender=Post)
def send_post_created_email_signal(sender, instance, created, **kwargs):
    if created:
        send_post_created_email(instance)
