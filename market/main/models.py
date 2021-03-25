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
    seller = models.ManyToManyField(Seller)
    title = models.CharField(max_length=255)
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    depth = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'
