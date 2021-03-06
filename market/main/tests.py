from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from main.models import Product, Category


class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(user)
        Category.objects.create(title='testcat')
        Product.objects.create(title='TestProduct1', category=Category.objects.get(title='testcat'))

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_goods(self):
        response = self.client.get(reverse('goods'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        response = self.client.get(reverse('product-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_goods_add(self):
        response = self.client.get(reverse('goods-add'))
        self.assertEqual(response.status_code, 200)

    def test_goods_edit(self):
        response = self.client.get(reverse('goods-edit', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
