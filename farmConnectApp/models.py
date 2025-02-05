from django.db import models
from django.contrib.auth.hashers import make_password


class ConsumerModel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)
        
    def __str__(self):
        return self.email