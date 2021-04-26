import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from main.models import Category, Product


@pytest.mark.django_db
class TestViews:

    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.client = Client()
        user = User.objects.create_superuser(username='testuser', password='12345')
        self.client.force_login(user)
        Category.objects.create(title='testcat')
        Product.objects.create(title='TestProduct1', category=Category.objects.get(title='testcat'))

    def test_index(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == 200

    def test_goods(self):
        response = self.client.get(reverse('goods'))
        assert response.status_code == 200

    def test_product_detail(self):
        response = self.client.get(reverse('product-detail', kwargs={'pk': 1}))
        assert response.status_code == 200

    def test_goods_add(self):
        response = self.client.get(reverse('goods-add'))
        assert response.status_code == 200

    def test_goods_edit(self):
        response = self.client.get(reverse('goods-edit', kwargs={'pk': 1}))
        assert response.status_code == 200
