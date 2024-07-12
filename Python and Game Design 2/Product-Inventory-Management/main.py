def load_products(file_name):
    products = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        product_info = {}
        for line in lines:
            line = line.strip()
            if line.startswith('Product'):
                if product_info:
                    products.append(product_info)
                product_info = {'Product': line.split(': ')[1]}
            elif line.startswith('Price'):
                product_info['Price'] = float(line.split(': ')[1])
            elif line.startswith('Stock'):
                product_info['Stock'] = int(line.split(': ')[1])
        if product_info:
            products.append(product_info)
    return products

def save_products(file_name, products):
    with open(file_name, 'w') as f:
        for product in products:
            f.write(f"Product: {product['Product']}\n")
            f.write(f"Price: {product['Price']}\n")
            f.write(f"Stock: {product['Stock']}\n")
            f.write("\n")

def display_products(products):
    for product in products:
        print(f"Product: {product['Product']}, Price: {product['Price']}, Stock: {product['Stock']}")

def add_products(products):
    product_name = input("Enter product name: ").strip()
    product_price = float(input("Enter product price: ").strip())
    product_stock = int(input("Enter product stock: ").strip())
    products.append({'Product': product_name, 'Price': product_price, 'Stock': product_stock})

def update_stock(products):
    product_name = input("Enter product name to update ").strip()
    for product in products:
        if product['Product'].lower() == product_name.lower():
            new_stock = int(input("Enter new stock quantity: ").strip())
            product['Stock'] = new_stock
            print(f"Stock updated for {product_name}.")
            return
        
    print("Product not found.")

if __name__ == "__main__":
    file_name = "products.txt"
    products = load_products(file_name)

    while True:
        print("\nProduct Inventory Management System")
        print("1. Display Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Save & Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_products(products)
        elif choice == '2':
            add_products(products)
        elif choice == '3':
            update_stock(products)
        elif choice == '4':
            save_products(file_name, products)
        else:
            print("Invalid choice. Please try again.")