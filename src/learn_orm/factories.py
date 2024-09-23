import factory
from .models import Author, Book
from faker import Faker

fake = Faker()


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.LazyAttribute(lambda _: fake.name())
    email = factory.LazyAttribute(lambda _: fake.email())


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=4))
    publication_date = factory.LazyAttribute(lambda _: fake.date())
    author = factory.SubFactory(AuthorFactory)
