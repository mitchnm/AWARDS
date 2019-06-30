from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to = 'awards/', null=True)
    bio = models.CharField(max_length=250, null=True)
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()

class Project(models.Model):
    image = models.ImageField(upload_to = 'awards/')
    project_name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
