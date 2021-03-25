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
    seller = models.ManyToManyField(Seller)
    title = models.CharField(max_length=255)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    depth = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'
