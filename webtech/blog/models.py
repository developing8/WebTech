from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField("Title", max_length=100)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    
    
