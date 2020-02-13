from django.db import models

# Create your models here.


class Portfolio(models.Model):
    image = models.ImageField(upload_to='image/')
    body = models.TextField()

    def __str__(self):
        return self.body[:10]






