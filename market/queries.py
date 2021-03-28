from market.main.models import Category, Product

Category.objects.create(title='smartphones')
Category.objects.create(title='tv')

new_product = Product(title='Iphone 100500', category=Category.objects.get(title='smartphones'))
new_product.save()

new_product = Product(title='Samsung 100500', category=Category.objects.get(title='smartphones'))
new_product.save()

new_product = Product(title='Sony TV 100500', category=Category.objects.get(title='tv'))
new_product.save()

new_product = Product(title='Gorizont TV 100500', category=Category.objects.get(title='tv'))
new_product.save()

print(Product.objects.filter(category__title='smartphones'))

