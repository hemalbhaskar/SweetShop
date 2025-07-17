# src/shop.py

class SweetShop:
    def __init__(self):
        self.next_id = 1
        self.sweets_menu = []

        # Initial sweets
        self.add_sweet("Rasgulla", "Mithai", 10, 20)
        self.add_sweet("Ladoo", "Mithai", 8, 25)
        self.add_sweet("Barfi", "Mithai", 12, 15)
        self.add_sweet("Swiss Roll", "Pastry", 30, 10)
        self.add_sweet("Dairy Milk", "Chocolate", 25, 18)

    def get_available_sweets(self):
        return self.sweets_menu

    def add_sweet(self, name, category, price, quantity):
        sweet = {
            'id': self.next_id,
            'name': name,
            'category': category,
            'price': price,
            'quantity': quantity
        }
        self.sweets_menu.append(sweet)
        self.next_id += 1

    def remove_sweet(self, sweet_id):
        self.sweets_menu = [item for item in self.sweets_menu if item['id'] != sweet_id]

    def search_by_name(self, name):
        return [s for s in self.sweets_menu if name.lower() in s['name'].lower()]

    def search_by_category(self, category):
        return [s for s in self.sweets_menu if category.lower() == s['category'].lower()]

    def search_by_price_range(self, min_price, max_price):
        return [s for s in self.sweets_menu if min_price <= s['price'] <= max_price]

    def purchase_sweet(self, sweet_id, quantity):
        for sweet in self.sweets_menu:
            if sweet['id'] == sweet_id:
                if sweet['quantity'] >= quantity:
                    sweet['quantity'] -= quantity
                    total_price = sweet['price'] * quantity
                    return sweet['name'], total_price, sweet['quantity']
                else:
                    raise ValueError(f"Only {sweet['quantity']} items available.")
        raise ValueError("Sweet not found.")

    def restock_sweet(self, sweet_id, quantity):
        for sweet in self.sweets_menu:
            if sweet['id'] == sweet_id:
                sweet['quantity'] += quantity
                return sweet['quantity']
        raise ValueError("Sweet not found.")
