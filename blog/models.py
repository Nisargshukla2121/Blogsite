from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.conf import settings # new
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    slug=models.CharField(max_length=130)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.title