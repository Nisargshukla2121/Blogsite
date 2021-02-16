from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now

STATUS_CHOICES = [
    ('General', 'General blog'),
    ('Study', "Study blog"),
    ('Technical', 'Technical Blog'),
]
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    slug=models.CharField(max_length=130)
    author = models.ForeignKey(User,  on_delete=models.CASCADE, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
   
  
def __str__(self):
        return self.title

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    
    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username



class BlogCategory(models.Model):   
   # [...]
   status = models.CharField(max_length=32,choices=STATUS_CHOICES, default="available",)