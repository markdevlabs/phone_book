class Phone:
    def __init__(self, brand: str, price: float):
        self.brand = brand
        self.price = price

new_phone = Phone("Samsung", 49500.55)
print(new_phone.brand)
print(new_phone.price)