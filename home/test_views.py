from django.test import TestCase
from .views import HomeView
from django.urls import reverse


class TestHomeView(TestCase):
    """
    Unit tests for homepage view
    """
    def setUp(self):
        self.url = reverse('home')

    def test_home_view(self):
        """
        Checks the correct response code and template
        is rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
