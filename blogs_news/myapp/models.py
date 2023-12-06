from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    image_url = models.URLField()
    published_at = models.DateTimeField(auto_now_add=True,null=True)
   
    
    class Meta:
        verbose_name = 'news article'
        verbose_name_plural = 'news articles'

    def __str__(self):
        return self.title



class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users_img/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title





