from django.test import TestCase


class TestOrm(TestCase):
    def test_author_factory(self):
        author = AuthorFactory()
