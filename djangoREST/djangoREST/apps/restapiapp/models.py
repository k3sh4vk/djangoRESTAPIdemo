from django.db import models

# Create your models here.

class webUsers(models.Model):
    username = models.CharField(max_length=10)
    email_id = models.CharField(max_length=20)

    def __str__(self):
        return self.username