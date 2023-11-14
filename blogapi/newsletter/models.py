from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    message = models.TextField(max_length=10000, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email
