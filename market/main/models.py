from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'


class Seller(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.first_name, self.last_name}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(default='description')  # add null=True later
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    depth = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'


class ProductInstance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(null=True)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.product.title, self.price}'

