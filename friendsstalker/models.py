from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User,null=True)
    text = models.TextField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.user
