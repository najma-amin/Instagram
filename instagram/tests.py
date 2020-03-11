from django.test import TestCase
from .models import Profile, Post


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user='najma', name = 'najma', profile_pic = 'home.png')
        self.profile.save()

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

class PostTestClass(TestCase):
    def setUp(self):
        self.post = Post(image = 'home.png', caption = "najma' post")
        self.post.save()

    def tearDown(self):
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))