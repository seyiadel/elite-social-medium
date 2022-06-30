from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Create your models here.

User = get_user_model()

class UserProfile(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =models.IntegerField()
    profileimage=models.ImageField(upload_to='profileimages')
    bio =models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Feedpost(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4())
    user=models.CharField(max_length=100)
    caption=models.CharField(max_length=200)
    postimage=models.ImageField(upload_to='post_images')
    created_at=models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.user