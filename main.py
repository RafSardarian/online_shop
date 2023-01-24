from product import Product
from user import User
from cart import ShoppingCart
from warehouse import Warehouse


product1 = Product("iPhone",899,"Electronics")
product2 = Product("T-shirt",25,"Clothes")
product3 = Product("Effective Python",55,"Books")
product4 = Product('Sony TV',1100,"Electronics")

product2.update_price(22)

user1 = User("Jack","Claymont,DE zip 19703","jack@gmail.com","4555 1200 9632 4512")

user1_cart = ShoppingCart(user1)
user1_cart.add_item(product2,2)
user1_cart.add_item(product4,3)
print(user1_cart.get_total())


main_warehouse = Warehouse()
main_warehouse.add_product(product1,100)
main_warehouse.add_product(product2,2000)
main_warehouse.add_product(product3,5005)
main_warehouse.add_product(product4,300)

print(main_warehouse.filter_by_category(("Electronics")))