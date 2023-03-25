from django.test import TestCase
from .forms import BlogForm, CommentForm


class TestBlogForm(TestCase):

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

    def test_image_field_is_not_required(self):
        form = BlogForm(
            {
                "created_by": "superuser90",
                "description": "This is a football post",
                "title": "Football Post",
                "blog_image": "",
                "body": "Test body",
                "category": "Football",
            }
        )
        self.assertTrue(form.is_valid())