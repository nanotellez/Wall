from django.db import models

from apps.login_registration.models import User

# Create your models here.


class Message(models.Model):
    content = models.TextField()
    posted_by = models.ForeignKey(User, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content=models.TextField()
    posted_by = models.ForeignKey(User, related_name='comments')
    on_message = models.ForeignKey(Message, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

