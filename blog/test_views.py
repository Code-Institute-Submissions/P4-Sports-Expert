from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BlogPost, Comments
from .forms import CommentForm
from .views import BlogList, BlogDetail


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


class TestBlogDetailView(TestCase):
    def setUp(self):
        """Creates valid comment database entry"""
        # Needed for created_by id non null constraint
        test_user = User.objects.create_user(
            username='testuser1', password='testpassword1'
        )
        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
            )

        self.blog_post = BlogPost.objects.create(
            created_by=test_user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )

        self.comment_form = CommentForm()

        self.comment_data = {
            'text': 'Test comment content'
        }

        self.comment = Comments.objects.create(
            comment='Test comment text',
            user=self.user,
            post=self.blog_post
            )

    def test_blog_detail_view(self):
        """
        Checks correct template, response code and form data is being rendered
        on the page
        """
        url = reverse('blog_detail', kwargs={'pk': self.blog_post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_detail.html')
        self.assertContains(response, self.blog_post.title)
        self.assertContains(response, self.blog_post.body)
        self.assertContains(response, self.comment.comment)
        self.assertIsInstance(response.context['form'], CommentForm)
        self.assertEqual(response.context['form'], self.comment_form)
        self.assertQuerysetEqual(
            response.context['comments'], [repr(self.comment)])

        def test_post_method_valid_form(self):
            url = reverse('blog_detail', kwargs={'pk': self.blog_post.pk})
            self.client.login(username='testuser', password='testpass')
            response = self.client.post(url, data=self.comment_data)
            self.assertRedirects(response, url)
            self.assertContains(response, "Your comment has been added")
            self.assertEqual(Comment.objects.count(), 2)
            new_comment = Comment.objects.get(content='Test comment content')
            self.assertEqual(new_comment.user, self.user)
            self.assertEqual(new_comment.post, self.blog_post)        







