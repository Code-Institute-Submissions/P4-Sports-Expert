from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, reverse_lazy
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from .models import BlogPost, Comments
from .forms import CommentForm
from .views import BlogList, BlogDetail, DeleteBlog, AddBlog, EditBlog
from .views import DeleteComment


class TestListView(TestCase):
    """
    Unit tests for blog list view
    """
    def setUp(self):
        """
        Creates valid comment database entry
        """
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
        """
        Checks the correct response code and template
        is rendered
        """
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
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass'
        )
        self.blogpost = BlogPost.objects.create(
            created_by=test_user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )
        self.comment_data = {
            'post': 'testpost',
            'comment': 'Test comment',
            'user': 'Test user',
        }
        self.form = CommentForm(data=self.comment_data)
        self.url = reverse('blog_detail', kwargs={'pk': self.blogpost.pk})
        self.client = Client()
        self.view = BlogDetail.as_view()
        self.factory = RequestFactory()

    def test_post_method(self):
        """
        Creates client to post comment data, checks the correct url
        and data is being rendered, correct response status code and
        correct page redirect
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url, data=self.comment_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse('blog_detail', kwargs={'pk': self.blogpost.pk}),
            status_code=302,
            target_status_code=200,
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your comment has been added')
        self.assertEqual(Comments.objects.count(), 1)

    def test_get_context_data(self):
        """
        Creates a blogpost and a request object,
        checks that the context contains the correct objects
        """
        post = self.blogpost
        request = self.factory.get(reverse('bloglist'))
        view = BlogList.as_view()
        context = view(request).context_data
        self.assertIn('object_list', context)
        self.assertIn('paginator', context)
        self.assertIn('page_obj', context)
        self.assertIn('is_paginated', context)
        self.assertEqual(len(context['object_list']), 1)
        self.assertEqual(context['object_list'][0], post)

    def test_view_returns_200_and_expected_content(self):
        """
        Checks that view returns correct status code and content
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test')
        self.assertContains(response, 'This is a test blogpost body')


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


class EditBlogTest(TestCase):
    """
    Unit Tests for edit blog view
    """
    def setUp(self):
        """Creates valid comment database entry"""
        # Needed for created_by id non null constraint
        test_user = User.objects.create_user(
            username='testuser1', password='testpassword1'
        )
        self.blogpost = BlogPost.objects.create(
            created_by=test_user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )
        self.new_data = {
            'created_by': 'test_user',
            'description': 'This is a new test',
            'title': 'New title',
            'body': 'New body',
            'category': 'Rugby',
        }
        self.url = reverse('edit_blog', kwargs={'pk': self.blogpost.pk})

    def test_edit_blog(self):
        """
        Inserts new form data, checks that its valid, checks that the
        correct reverse url is rendered and checks that
        the correct user message is rendered
        """
        response = self.client.post(self.url, data=self.new_data, follow=True)
        self.assertRedirects(response, reverse('bloglist'))
        updated_blogpost = BlogPost.objects.get(pk=self.blogpost.pk)
        self.assertEqual(updated_blogpost.title, self.new_data['title'])
        self.assertEqual(updated_blogpost.body, self.new_data['body'])
        self.assertEqual(updated_blogpost.category, self.new_data['category'])
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Blog post edited successfully")


class TestDeleteComment(TestCase):
    """
    Unit tests for delete comment view
    """
    def setUp(self):
        """
        Creates valid comment database entry
        """
        # Needed for created_by id non null constraint
        test_user = User.objects.create_user(
            username='testuser1', password='testpassword1'
        )
        self.blogpost = BlogPost.objects.create(
            created_by=test_user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )
        self.comment = Comments.objects.create(
            post=self.blogpost,
            user=self.blogpost.created_by,
            comment='This is a test comment'
        )
        self.url = reverse_lazy(
            'delete_comment', kwargs={'pk': self.comment.pk}
            )

    def test_delete_comment(self):
        """
        Checks that the correct status code is returned, 
        checks that the comment no longer exists after being deleted
        and checks correct success message is rendered
        """
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comments.objects.filter(pk=self.comment.pk).exists())
        storage = get_messages(response.wsgi_request)
        self.assertEqual(
            list(storage)[0].message, 'Your comment has been deleted'
            )

    def test_get_success_url(self):
        """
        Checks correct success url is rendered after comment is
        deleted by user
        """
        view = DeleteComment()
        view.object = self.comment
        url = view.get_success_url()
        self.assertEqual(
            url, reverse_lazy('blog_detail', kwargs={'pk': self.blogpost.pk})
            )













