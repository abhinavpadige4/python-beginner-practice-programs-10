"""
Program 9: Nest dictionaries - inventory of products with price and stock
Concept: Dictionaries - nested dictionaries
"""

def demonstrate_nested_dictionary():
    """Demonstrate nested dictionaries for product inventory."""
    
    # Create nested dictionary for product inventory
    inventory = {
        "Laptop": {
            "price": 999.99,
            "stock": 15,
            "category": "Electronics"
        },
        "Mouse": {
            "price": 29.99,
            "stock": 50,
            "category": "Electronics"
        },
        "Keyboard": {
            "price": 79.99,
            "stock": 30,
            "category": "Electronics"
        },
        "Notebook": {
            "price": 4.99,
            "stock": 100,
            "category": "Office Supplies"
        },
        "Pen": {
            "price": 1.99,
            "stock": 200,
            "category": "Office Supplies"
        }
    }
    
    print("Product Inventory:")
    print("=" * 50)
    
    # Display all products
    for product, details in inventory.items():
        print(f"Product: {product}")
        print(f"  Price: ${details['price']:.2f}")
        print(f"  Stock: {details['stock']} units")
        print(f"  Category: {details['category']}")
        print()
    
    # Demonstrate accessing specific product info
    print("Accessing specific product information:")
    product_name = "Laptop"
    if product_name in inventory:
        product_info = inventory[product_name]
        print(f"{product_name}:")
        print(f"  Price: ${product_info['price']:.2f}")
        print(f"  Stock: {product_info['stock']} units")
    print()
    
    # Demonstrate updating stock
    print("Updating stock after sale:")
    product_to_sell = "Mouse"
    quantity_sold = 3
    
    if product_to_sell in inventory and inventory[product_to_sell]["stock"] >= quantity_sold:
        inventory[product_to_sell]["stock"] -= quantity_sold
        print(f"Sold {quantity_sold} {product_to_sell}(s)")
        print(f"Remaining stock: {inventory[product_to_sell]['stock']} units")
    else:
        print(f"Insufficient stock for {product_to_sell}")
    print()
    
    # Demonstrate adding new product
    print("Adding new product:")
    inventory["Desk Lamp"] = {
        "price": 19.99,
        "stock": 25,
        "category": "Home Office"
    }
    print("Added Desk Lamp to inventory")
    print(f"Desk Lamp details: {inventory['Desk Lamp']}")
    print()
    
    # Show updated inventory
    print("Updated Inventory Summary:")
    print("-" * 30)
    total_products = len(inventory)
    total_value = sum(details["price"] * details["stock"] for details in inventory.values())
    print(f"Total products: {total_products}")
    print(f"Total inventory value: ${total_value:.2f}")

if __name__ == "__main__":
    demonstrate_nested_dictionary()