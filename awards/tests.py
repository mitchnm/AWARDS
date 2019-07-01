from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Profile,Image,Comment

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='a')
        self.newimage = Image(image='media/insta/Fashion.jpg',image_name='Fashion',id =1,caption='Delicious',profile=self.user,likes=1)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.newimage,Image))

    def test_save_image(self):
        self.newimage.save()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id =1,username='a')
        self.new_profile = Profile(name=self.user, profile_pic='media/instagram/photo.jpg',bio='I am awesome')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_image(self):
        self.new_profile.save()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id =1,username='a')
        self.newimage = Image(image='media/insta/Fashion.jpg',image_name='Fashion',id =1,caption='Delicious',profile=self.user,likes=1)
        self.new_comment = Comment(user=self.user,image=self.new_image,comment='You are awesome',)
   
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))
