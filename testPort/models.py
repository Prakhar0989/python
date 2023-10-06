from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=250,default='')
    email = models.CharField(max_length=250,default='')
    password = models.CharField(max_length=250, default='')
    profile_image = models.FileField(upload_to='profile_images.jpg/',default='')
    # profile_image = models.FileField(default='default_profile_image.jpg',default="")

    class Meta:
        db_table = "UserProfile"

