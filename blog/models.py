from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    slug=models.CharField(max_length=130)
    author = models.ForeignKey(User,  on_delete = models.SET_NULL, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.title