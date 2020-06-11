from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserAccountProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    image = models.ImageField(default='default.jpg', upload_to='pics')


