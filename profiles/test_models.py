from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class TestProfileModel(TestCase):
    """
    Unit tests for profile model
    """
    def setUp(self):
        """
        Create a user object and link it to a profile object
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_profile_model_str_method(self):
        """
        Test that the __str__ method of the Profile model returns the username
        of the linked user object
        """
        expected_str_ = f'{self.user.username}'
        self.assertEqual(str(self.profile), expected_str_)
