from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='images', blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile',blank=True,null=True)
    contact = models.IntegerField(null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    url= models.URLField(null=True,blank=True)