from django.db import models
from django.contrib.auth.models import User

# Create your models here.  
class UserImage(models.Model):  
    image = models.ImageField(upload_to='images', null=True, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="image"
    )  
  
    def __str__(self):  
        return self.user.username  
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
        	url = ''
        return url