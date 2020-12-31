from django.db import models
from .post import Post
from django.contrib.auth.models import User






class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    #tuple for the choices
    LIKE_CHOICES = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike')
    )
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=50)


    def __str__(self):
        return str(self.post)
