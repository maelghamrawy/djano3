from django.db import models

# Create your models here.

class login(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.email}"