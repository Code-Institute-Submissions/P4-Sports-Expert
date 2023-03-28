from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile, BlogPost
from .views import ProfileView, MyBlogs


class TestProfileView(TestCase):
    """
    Unit tests for profile detail view
    """
    def setUp(self):
        """
        Creates client user and links to profile
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass',
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_profile_detail_view_get_method(self):
        """
        Uses client profile to send a get request to
        profile view using username as a paramater, checks correct
        status code response and correct context is returned
        """
        response = self.client.get(
            reverse('profile', args=[self.user.username])
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertEqual(response.context['profile'], self.profile)


class TestMyBlogsView(TestCase):
    """
    Unit tests for myblogs view
    """
    def setUp(self):
        """
        Creates valid comment database entry
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.blogpost = BlogPost.objects.create(
            created_by=self.user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )

    def test_get_queryset_method(self):
        """
        Logs in as test user using client and makes a get request
        to the myblogs url, checks that correct response code is returned
        , checks that the created test blogpost is in the context_data queryset
        """
        self.client.login(username='testuser', password='testpass')
        url = reverse('myblogs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        queryset = response.context_data['object_list']
        self.assertEqual(queryset.count(), 1)
        self.assertIn(self.blogpost, queryset)
