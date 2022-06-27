from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class UserProfile(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =models.IntegerField()
    profileimage=models.ImageField(upload_to='profileimages')
    bio =models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

        


