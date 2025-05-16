from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    phone=models.CharField(max_length=11)
    avatar=models.ImageField(upload_to='avatar',null=True)
    sign=models.CharField(max_length=50)
    info=models.TextField()
    update_time=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='user_profile'
