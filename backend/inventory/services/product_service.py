from ..models import Product


tempList = [{'name': 'Product1'}, {'name': 'Product2'}]


def get_all_products():
    return tempList

def get_product_by_id(product_id: str):
    return Product.objects.get(id = product_id)

def add_product(products: list):
    list_of_products = [Product(productName=p['name'], price=p['price']) for p in products]
    Product.objects.bulk_create(list_of_products)

def update_product(product: Product):
    currentProduct = get_product_by_id(product['id'])
    Product.objects.all().remove(currentProduct)
    Product.objects.all().add(product)

def delete_product(products):
    list_of_products = [Product(productName=p['name'], price=p['price']) for p in products]
    Product.objects.bulk_remove(list_of_products)

def __str__(self):
    return self.name
