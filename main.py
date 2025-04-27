import pandas as pd
try:
    inventory = pd.read_csv("inventory.csv")
except FileNotFoundError:
    data = {
        'Item': ['Rice (kg)', 'Atta (kg)', 'Dal (kg)', 'Sugar (kg)', 'Oil (liter)', 'Spices (pkt)', 'Tea (pkt)', 'Biscuits (pkt)'],
        'Quantity': [100, 50, 60, 30, 20, 50, 30, 128],
        'Price': [60, 40, 45, 30, 180, 30, 20, 28]
    }
    inventory = pd.DataFrame(data)
    inventory.to_csv("inventory.csv", index=False)
def update_inventory(item, quantity):
    if item in inventory['Item'].values:
        index = inventory[inventory['Item'] == item].index[0]
        if inventory.at[index, 'Quantity'] >= quantity:
            inventory.at[index, 'Quantity'] -= quantity
            print(f"{quantity} {item} sold.")
        else:
            print(f"Not enough {item} in stock.")
    else:
        print(f"{item} not found in inventory.")
def generate_bill(items, quantities):
    total_bill = 0
    print("\n=== Bill ===")
    for item, quantity in zip(items, quantities):
        if item in inventory['Item'].values:
            index = inventory[inventory['Item'] == item].index[0]
            price = inventory.at[index, 'Price']
            cost = price * quantity
            total_bill += cost
            print(f"{quantity} {item}: {cost:.2f}")
        else:
            print(f"{item} not found in inventory.")
    print(f"Total: {total_bill:.2f}\n")
    return total_bill
def check_low_stock(threshold=20):
    low_stock_items = inventory[inventory['Quantity'] < threshold]['Item'].tolist()
    if low_stock_items:
        print("Low stock alert:", low_stock_items)
    else:
        print("All items are sufficiently stocked.")
def save_inventory():
    inventory.to_csv("inventory.csv", index=False)
    print("Inventory saved.")
def menu():
    while True:
        print("\n1. Update Inventory")
        print("2. Generate Bill")
        print("3. Check Low Stock")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            update_inventory(item, quantity)
        elif choice == '2':
            items = input("Enter items (comma-separated): ").split(',')
            quantities = list(map(int, input("Enter quantities (comma-separated): ").split(',')))
            generate_bill(items, quantities)
        elif choice == '3':
            check_low_stock()
        elif choice == '4':
            save_inventory()
            break
        else:
            print("Invalid choice. Please try again.")
if _name_== "_main_":
    menu()
