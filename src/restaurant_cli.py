class RestaurantCLI:
    def __init__(self, database):
        self.database = database

    def display_product_details(self, product):
        if product:
            print("Product Details:")
            print(f"Name: {product['name']}")
            print(f"Description: {product['description']}")
            print(f"Price: ${product['price']}")
            print(f"Restaurant Chain: {product['chain_name']}")
        else:
            print("Product not found.")

    def run(self):
        while True:
            print("\nRestaurant Chain Database")
            print("1. Search for product by ID")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                product_id = input("Enter product ID: ")
                product = self.database.search_product(product_id)
                self.display_product_details(product)
            elif choice == '2':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
