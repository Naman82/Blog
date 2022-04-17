from django.db import models

# Create your models here.
class Post(models.Model):
    content=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='images', blank=True, null=True)