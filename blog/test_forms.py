from django.test import TestCase
from .forms import BlogForm, CommentForm
from .models import BlogPost
from django.contrib.auth.models import User


class TestBlogForm(TestCase):
    """Unit tests for blogform"""
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_form_fields(self):
        """
        Tests that the form fields are set correctly
        """
        form = BlogForm()
        self.assertEqual(len(form.fields), 6)
        self.assertIn('description', form.fields)
        self.assertIn('title', form.fields)
        self.assertIn('blog_image', form.fields)
        self.assertIn('body', form.fields)
        self.assertIn('category', form.fields)
        self.assertIn('created_by', form.fields)

    def test_form_user_disabled(self):
        """
        Tests that the user field is disabled
        """
        form = BlogForm(instance=BlogPost(created_by=self.user))
        self.assertTrue(form.fields['created_by'].disabled)

    def test_blogform_body_is_required(self):
        """Checks if form is invalid with blank body"""
        form = BlogForm(
            {
                "created_by": "superuser90",
                "description": "This is a football post",
                "title": "Football Post",
                "blog_image": "test.jpg",
                "body": "",
                "category": "Football",
            }
            )
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_image_field_must_be_file(self):
        """Checks if form is invalid with integer in image field"""
        form = BlogForm(
            {
                "created_by": "superuser90",
                "description": "This is a football post",
                "title": "Football Post",
                "blog_image": 0,
                "body": "Test body",
                "category": "Football",
            }
        )
        self.assertFalse(form.is_valid())


class TestCommentForm(TestCase):
    """Unit tests for comment form"""
    def setUp(self):
        """Creates valid comment database entry"""
        # Needed for non null created_by constraint
        test_user = User.objects.create_user(
            username='testuser2', password='testpassword1'
        )
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.blog_post = BlogPost.objects.create(
            created_by=test_user,
            description="This is a test",
            title="This is a test blogpost title",
            body='This is a test blogpost body',
            category='Football',
        )

    def test_comment_form_is_valid(self):
        """Tests comment form is valid with mock values"""
        form_data = {'comment': 'This is a test comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_commentform_body_empty(self):
        """Test comment form is invalid with empty body"""
        form = CommentForm({"comment": ""})
        self.assertIn("comment", form.errors.keys())
        self.assertEqual(form.errors["comment"][0], "This field is required.")
        self.assertFalse(form.is_valid())
