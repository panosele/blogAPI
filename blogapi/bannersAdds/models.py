from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/bannerAdds')
    date = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.title