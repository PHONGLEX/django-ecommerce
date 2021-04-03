from unittest import skip

from django.test import TestCase, RequestFactory
from django.http import HttpRequest
from django.contrib.auth.models import User

from store.models import Category, Product
from django.test import Client
from django.shortcuts import reverse

from store.views import all_products


class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name="django", slug="django")
        User.objects.create(username="admin")
        user = User.objects.first()
        category = Category.objects.first()
        self.data1 = Product.objects.create(
            category_id=category.id,
            title="django beginners",
            created_by_id=user.id,
            slug="django-beginners",
            price="20.00",
            image="django",
        )

    def test_url_allowed_host(self):
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(
            reverse("store:product_detail", args=["django-beginners"])
        )
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse("store:category_list", args=["django"]))
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode("utf8")
        self.assertNotIn("<title>Home</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get("/django-beginners")
        response = all_products(request)
        html = response.content.decode("utf8")
        self.assertNotIn("<title>Home</title>", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_url_allowed_host(self):
        response = self.c.get("/", HTTP_HOST="noaddress.com")
        self.assertEqual(response.status_code, 400)
        reponse = self.c.get("/", HTTP_HOST="yourdomain.com")
        self.assertEqual(response.status_code, 200)