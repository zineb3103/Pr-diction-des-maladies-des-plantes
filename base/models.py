from django.db import models

# Create your models here.
class Base(models.Model):
    user = models.CharField(max_length=30)
    genre = models.CharField(max_length=5)
    email = models.EmailField(unique=True, max_length=100)
    pwd = models.CharField(max_length=15)

    def __str__(self):
        return self.user