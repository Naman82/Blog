from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='images', blank=True, null=True)