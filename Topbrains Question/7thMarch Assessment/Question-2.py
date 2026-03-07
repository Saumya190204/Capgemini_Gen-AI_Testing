# Question-2-Product Stock Shortage Report

class Solution:
    def low_stock_products(self, inventory):
        result = []
        
        for product, quantity in inventory.items():
            if quantity < 10:
                result.append(product)
                
        return result