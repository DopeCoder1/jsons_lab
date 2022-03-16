from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.name
