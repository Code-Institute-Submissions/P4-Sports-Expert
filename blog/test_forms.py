from django.test import TestCase
from .forms import BlogForm, CommentForm
from .models import BlogPost
from django.contrib.auth.models import User


class TestBlogForm(TestCase):
    """Unit tests for blogform"""
    def test_blogform_is_valid(self):
        """Test blog form is valid"""
        form = BlogForm(
            {
                "created_by": "superuser90",
                "description": "This is a football post",
                "title": "Football Post",
                "blog_image": "test.jpg",
                "body": "This is the post body",
                "category": "Football",
            }
        )
        self.assertTrue(form.is_valid())

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
    def comment_form_is_valid(self):
        """Test form is valid"""
        form = CommentForm({"comment": "Great write up"})
        self.assertTrue(form.is_valid())

    def test_commentform_body_empty(self):
        """Test comment form is invalid with empty body"""
        form = CommentForm({"comment": ""})
        self.assertIn("comment", form.errors.keys())
        self.assertEqual(form.errors["comment"][0], "This field is required.")
        self.assertFalse(form.is_valid())

