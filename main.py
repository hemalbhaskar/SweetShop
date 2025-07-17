# main.py

from src.shop import SweetShop

def print_table(sweets):
    if not sweets:
        print("⚠️ No matching sweets found.")
        return

    print("┌────┬────────────┬────────────┬────────┬────────────┐")
    print("│ ID │ Name       │ Category   │ Price  │ Quantity   │")
    print("├────┼────────────┼────────────┼────────┼────────────┤")
    for s in sweets:
        print(f"│ {str(s['id']).ljust(2)} │ {str(s['name']).ljust(10)} │ {str(s['category']).ljust(10)} │ ₹{str(s['price']).ljust(5)} │ {str(s['quantity']).ljust(10)} │")
    print("└────┴────────────┴────────────┴────────┴────────────┘")

def print_menu(shop):
    print("\n🧁 Sweet Shop Menu:")
    print_table(shop.get_available_sweets())

def search_menu(shop):
    print("\n======================")
    print("🔍 Search Menu")
    print("======================")
    print("1. Search by Name")
    print("2. Search by Category")
    print("3. Search by Price Range")
    choice = input("Enter your choice (1–3): ")

    if choice == '1':
        name = input("Enter sweet name to search: ")
        result = shop.search_by_name(name)
        print("\n✅ Results:")
        print_table(result)

    elif choice == '2':
        category = input("Enter category to search: ")
        result = shop.search_by_category(category)
        print("\n✅ Results:")
        print_table(result)

    elif choice == '3':
        try:
            min_price = int(input("Enter min price: "))
            max_price = int(input("Enter max price: "))
            result = shop.search_by_price_range(min_price, max_price)
            print("\n✅ Results:")
            print_table(result)
        except ValueError:
            print("❌ Price should be a number.")
    else:
        print("⚠️ Invalid search option.")

def main():
    shop = SweetShop()
    while True:
        print("\n======================")
        print("🍬 Sweet Shop System")
        print("======================")
        print("1. Show Menu")
        print("2. Add Sweet")
        print("3. Remove Sweet by ID")
        print("4. Exit")
        print("5. Search Sweets")
        print("6. Purchase Sweet")
        print("7. Restock Sweet")

        choice = input("Enter your choice (1–7): ")

        if choice == '1':
            print_menu(shop)

        elif choice == '2':
            name = input("Enter sweet name: ")
            category = input("Enter category (Mithai/Chocolate/Pastry/Candy): ")
            try:
                price = int(input("Enter price: "))
                quantity = int(input("Enter quantity in stock: "))
                shop.add_sweet(name, category, price, quantity)
                print(f"✅ {name} added to the menu.")
            except ValueError:
                print("❌ Price and quantity must be numbers.")

        elif choice == '3':
            try:
                sweet_id = int(input("Enter sweet ID to remove: "))
                shop.remove_sweet(sweet_id)
                print(f"❌ Sweet with ID {sweet_id} removed.")
            except ValueError:
                print("❌ ID must be a number.")

        elif choice == '4':
            print("👋 Exiting Sweet Shop. Bye!")
            break

        elif choice == '5':
            search_menu(shop)

        elif choice == '6':
            try:
                sweet_id = int(input("Enter Sweet ID to buy: "))
                quantity = int(input("Enter quantity: "))
                name, total, remaining = shop.purchase_sweet(sweet_id, quantity)
                print(f"\n✅ You ordered: {name} x{quantity}")
                print(f"💰 Total Price: ₹{total}")
                print(f"📦 Remaining Stock: {remaining}")
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == '7':
            try:
                sweet_id = int(input("Enter Sweet ID to restock: "))
                quantity = int(input("Enter quantity to add: "))
                updated_qty = shop.restock_sweet(sweet_id, quantity)
                print(f"✅ Stock updated! New quantity: {updated_qty}")
            except ValueError as e:
                print(f"❌ {e}")

        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
