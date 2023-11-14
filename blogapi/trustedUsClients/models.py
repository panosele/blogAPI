from django.db import models

# Create your models here.
class TrustedUsClients(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/trusted_us_clients')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
