from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from .models import BlogPost, Comments
from .forms import CommentForm
from .views import BlogList, BlogDetail, DeleteBlog, AddBlog


class TestListView(TestCase):
    """Unit tests for blog list view"""
    def setUp(self):
        """Creates valid comment database entry"""
        # Needed for created_by id non null constraint
        test_user = User.objects.create_user(
            username='testuser', password='testpassword1'
        )
        self.url = reverse('bloglist')
        self.blogpost = BlogPost.objects.create(
            created_by=test_user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )

    def test_blog_list_view(self):
        """Checks the correct response code and template
        is rendered"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_home.html')


class TestAddBlogView(TestCase):
    """
    Unit Tests for add blog view
    """
    def setUp(self):
        """
        Creates valid comment database entry
        """
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('add_blog')

    def test_add_blog_form(self):
        """
        Test add blog form
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, 'type="submit"')

    def test_url_accessible_by_name(self):
        """
        Tests url name returns a valid 200 response
        """
        response = self.client.get(reverse('add_blog'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Tests url renders correct template
        """
        response = self.client.get(reverse('add_blog'))
        self.assertTemplateUsed(response, 'add_blog.html')

    def test_add_blog_initial(self):
        """
        Tests add blog initial method
        """
        response = self.client.get(self.url)
        form = response.context_data['form']
        self.assertEqual(form.initial['created_by'], self.user)    


class TestDeleteBlogView(TestCase):
    def setUp(self):
        """Creates valid comment database entry"""
        # Needed for created_by id non null constraint
        test_user = User.objects.create_user(
            username='testuser1', password='testpassword1'
        )
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.blogpost = BlogPost.objects.create(
            created_by=test_user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )
        self.url = reverse('delete_blog', args=[self.blogpost.pk])
        self.client.login(username='testuser', password='testpassword')

    def test_delete_blog_page(self):
        """
        Checks correct template is rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_blog.html')

    def test_delete_blog(self):
        """
        Checks message is rendered correctly when post is deleted
        """
        response = self.client.post(self.url, follow=True)
        self.assertRedirects(response, reverse('bloglist'))
        self.assertFalse(BlogPost.objects.filter(pk=self.blogpost.pk).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Blog post deleted successfully")












