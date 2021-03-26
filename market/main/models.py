from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'


class Seller(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    depth = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'


class ProductInstance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(null=True)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.product.title, self.price}'

