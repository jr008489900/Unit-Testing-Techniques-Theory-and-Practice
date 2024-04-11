import unittest

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def addToCart(self, productId, quantity):
        if productId in self.items:
            self.items[productId] += quantity
        else:
            self.items[productId] = quantity

    def calculateTotalPrice(self):
        total = 0
        for productId, quantity in self.items.items():
            # 假設產品價格是固定的10元
            price = 10
            total += price * quantity
        return total

class TestShoppingCart(unittest.TestCase):
    def test_calculateTotalPrice(self):
        # 初始化購物車並添加產品
        cart = ShoppingCart()
        cart.addToCart('P001', 2)
        cart.addToCart('P002', 1)
        
        assert cart.items == {'P001':2,'P002':1}

        # 測試calculateTotalPrice
        total = cart.calculateTotalPrice()
        assert total == 30