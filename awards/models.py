from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to = 'awards/',blank=True)
    bio = models.CharField(max_length=250, null=True)
    
    # @classmethod
    # def search_by_name(cls,search_term):
    #     profile = cls.objects.filter(name__icontains=search_term)
    #     return profile

    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()

class Project(models.Model):
    image = models.ImageField(upload_to = 'awards/')
    project_name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, null=True)

class Rating(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10')
    )
    project = models.ForeignKey('Project')
    user = models.ForeignKey(User)
    design = models.IntegerField(choices=RATING)
    usability = models.IntegerField(choices=RATING)
    content = models.IntegerField(choices=RATING)
    comment = models.CharField(max_length=500)

class AwardsMerch(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_pic = models.ImageField(upload_to = 'awards/',blank=True)
    bio = models.CharField(max_length=250, null=True)

class ProjectMerch(models.Model):
    image = models.ImageField(upload_to = 'awards/')
    project_name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)

