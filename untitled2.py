class Product:
    def __init__(self, name, price, stock):
        
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
       
        if quantity > self.stock:
            raise ValueError("На складі недостатньо товару.")
        self.stock -= quantity

    def __str__(self):
      
        return f"Назва: {self.name}, Ціна: {self.price:.2f}, Наявність: {self.stock}"


class Cart:
    def __init__(self):
       
        self.items = {}

    def add_product(self, product, quantity):
        
        if quantity > product.stock:
            print(f"Недостатньо товару '{product.name}' на складі!")
            return
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {
                'product': product,
                'quantity': quantity
            }
        product.reduce_stock(quantity)
        print(f"Товар '{product.name}' у кількості {quantity} додано до кошика!")

    def remove_product(self, product_name, quantity):
        
        if product_name not in self.items:
            print(f"Товар '{product_name}' не знайдено в кошику!")
            return
        item = self.items[product_name]
        if quantity >= item['quantity']:
            item['product'].stock += item['quantity']
            del self.items[product_name]
            print(f"Товар '{product_name}' повністю видалено з кошика!")
        else:
            item['product'].stock += quantity
            item['quantity'] -= quantity
            print(f"Кількість товару '{product_name}' зменшено на {quantity} в кошику.")

    def total_price(self):
      
        return sum(item['product'].price * item['quantity'] for item in self.items.values())

    def show_cart(self):
       
        if not self.items:
            print("Кошик порожній.")
        else:
            print("Товари в кошику:")
            for item in self.items.values():
                product = item['product']
                quantity = item['quantity']
                print(f"- {product.name} | Ціна: {product.price:.2f} | Кількість: {quantity}")


if __name__ == "__main__":
    
    product1 = Product("Ноутбук", 25000, 10)
    product2 = Product("Мишка", 500, 50)
    product3 = Product("Навушники", 1500, 20)

   
    print(product1)
    print(product2)
    print(product3)

   
    cart = Cart()

   
    cart.add_product(product1, 2)
    cart.add_product(product2, 5)
    cart.add_product(product3, 1)

    
    print("\nВаш кошик:")
    cart.show_cart()

   
    cart.remove_product("Мишка", 2)

    
    print("\nОновлений кошик:")
    cart.show_cart()

    
    print(f"\nЗагальна вартість: {cart.total_price():.2f} грн")
