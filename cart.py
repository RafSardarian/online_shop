class ShoppingCart:
    def __init__(self,user):
        self.user = user
        self.items = {}

    def add_item(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]['Quantity'] += quantity
        else:
            self.items[product.name] = {'Product':product,'Quantity':quantity}


    def remove_item(self,product,quantity):
        if product.name in self.items:
            if self.items[product.name]['Quantity'] > quantity:
                self.items[product.name]['Quantity'] -= quantity
            else:
                self.items[product.name] = {'Product':product,'Quantity':quantity}

    def get_total(self):
        total = 0
        for item in self.items.values():
            total += item['Product'].price * item['Quantity']
        return total



