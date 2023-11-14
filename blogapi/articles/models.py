from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    article_body = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=80, default="")
    date = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.title