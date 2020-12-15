from django.db import models
from .post import Post





class Comment(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    

    class Meta:
        verbose_name = ("comment")
        verbose_name_plural = ("comments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})
