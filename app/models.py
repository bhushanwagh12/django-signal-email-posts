from django.db import models
from django.contrib.auth.models import User
from .utils import send_post_created_email
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title








