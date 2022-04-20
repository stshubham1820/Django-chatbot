from email.message import Message
from django.db import models

# Create your models here.
class form(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Email = models.EmailField(null=True)
    Message = models.CharField(max_length=100,null=True)
    Review = models.TextField(null=True)