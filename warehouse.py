class Warehouse:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product.name in self.products:
            self.products[product.name]['Quantity'] += quantity
        else:
            self.products[product.name] = {'Product':product,'Quantity':quantity}

    def reemove_product(self, product, quantity):
        if product.name in self.products:
            if self.products[product.name]['Quantity'] > quantity:
                self.products[product.name]['Quantity'] -= quantity
            else:
                del self.products[product.name]

    def filter_by_category(self,category):
        filtered_products = {}
        for product in self.products.values():
            if product['Product'].categories == category:
                filtered_products[product['Product'].name] = product
        return filtered_products
