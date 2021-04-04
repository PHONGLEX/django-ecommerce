from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings


from store.models import Product, Category


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username="admin")
        Category.objects.create(name="django", slug="django")
        user = User.objects.first()
        category = Category.objects.first()
        Product.objects.create(
            category_id=category.id,
            title="django beginners",
            created_by_id=user.id,
            slug="django-beginners",
            price="20.00",
            image="django",
        )
        Product.objects.create(
            category_id=category.id,
            title="django intermediate",
            created_by_id=user.id,
            slug="django-intermediate",
            price="40.00",
            image="django",
        )
        Product.objects.create(
            category_id=category.id,
            title="django advanced",
            created_by_id=user.id,
            slug="django-advanced",
            price="60.00",
            image="django",
        )
        self.client = Client()
        self.client.post(
            reverse("basket:basket_add"),
            {"productid": 1, "productqty": 1, "action": "post"},
            xhr=True,
        )
        self.client.post(
            reverse("basket:basket_add"),
            {"productid": 2, "productqty": 2, "action": "post"},
            xhr=True,
        )

    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse("basket:basket_summary"))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        response = self.client.post(
            reverse("basket:basket_add"),
            {"productid": 3, "productqty": 1, "action": "post"},
            xhr=True,
        )
        self.assertEqual(response.json(), {"qty": 4})
        response = self.client.post(
            reverse("basket:basket_add"),
            {"productid": 2, "productqty": 1, "action": "post"},
            xhr=True,
        )
        self.assertEqual(response.json(), {"qty": 5})

    def test_basket_delete(self):
        """
        Test deleting items from the basket
        """
        response = self.client.get(reverse("basket:basket_summary"))
        print(response)

        response = self.client.post(
            reverse("basket:basket_delete"),
            {"productid": 2, "action": "post"},
            hxr=True,
        )
        self.assertEqual(response.json(), {"qty": 1, "subtotal": "20.00"})

    def test_basket_update(self):
        """
        Test updating items from the basket
        """
        response = self.client.post(
            reverse("basket:basket_delete"),
            {"productid": 2, "productqty": 1, "action": "post"},
            xhr=True,
        )
        self.assertEqual(response.json(), {"qty": "2", "subtotal": "60.00"})
