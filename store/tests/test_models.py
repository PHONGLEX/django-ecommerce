from django.test import TestCase
from django.contrib.auth import get_user_model

from store.models import Category, Product

User = get_user_model()


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug="django")

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), "django")


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="admin")
        category = Category.objects.first()
        user = User.objects.first()
        self.data1 = Product.objects.create(
            category_id=category.id,
            title="django beginners",
            created_by_id=user.id,
            slug="django-beginners",
            price="20.00",
            image="django",
        )

    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "django beginners")
