import factory

from product.models import Product
from product.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('py str')
    slug = factory.Faker('py str')
    description = factory.Faker('py str')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('pyint')
    category = factory.LazyAttribute(CategoryFactory)
    title = factory.Faker('py str')

    @factory.post_generation
    def category(self, create, extracted):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Product
