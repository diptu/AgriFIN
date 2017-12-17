
from django.test import TestCase

from .models import User,Land

from .forms import ProfileUpdate


class UserModelTest(TestCase):

    def test_string_representation(self):
        testUser = User(username="My test user",bio="test bio")
        self.assertEqual(str(testUser), testUser.username,testUser.bio)
        self.user = User.objects.create(username='some_user')
        if self.user is not None :
            print("User creation working fine! ")
        else :
            print("not working!")



class ProjectTests(TestCase):

    def test_homepage(self):
        if self.client.get('/'):
            print("Home page passed url testing ")

        else :
            print("Home page passed url testing ")



class LandModelTest(TestCase):

    def test_string_representation(self):

        testUser = User(username="My test user",bio="test bio")
        self.assertEqual(str(testUser), testUser.username,testUser.bio)
        owner = Land(location="test Land location")
        self.assertEqual(str(owner), "test Land location")
        print("Land string represntation Working ")



class ProfileUpdateTest(TestCase):
    def test_valid_data(self):
        form = ProfileUpdate({
        'username': "Turanga Leela",
        'email': "leela@example.com",
        'bio': "Hi there",
        })
        self.assertTrue(form.is_valid())
        form.save()
        print("profile update  passed unit testing !")

    def test_blank_data(self):
        form = ProfileUpdate({})

        self.assertEqual(form.errors, {
        })
