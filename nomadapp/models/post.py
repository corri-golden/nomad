from django.db import models
from django.contrib.auth.models import User





class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=255, blank=True, default=None)
    # slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True, default='')
    date = models.DateField(auto_now=False, auto_now_add=False,)
    liked = models.ManyToManyField(User, default=None,blank=True,related_name='liked')
    # description_html = models.TextField(editable=False,default='',blank=True)
    post_image = models.ImageField(blank=True, upload_to='images/')
    

    

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
