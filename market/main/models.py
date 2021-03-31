from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Seller(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.first_name, self.last_name}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  # add null=True later
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

    def get_tags(self):
        return {tag.tag_name for tag in self.tags.all()}


class ProductInstance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.product.title}'


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.tag_name}'


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
