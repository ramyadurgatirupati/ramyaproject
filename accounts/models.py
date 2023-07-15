from django.db import models
from django.contrib.auth.models import User
from django .db.models.signals import pre_save

# Create your models here.


class accounts(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password1 = models.CharField(max_length=200, null=True)
    password2 = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['password1']
