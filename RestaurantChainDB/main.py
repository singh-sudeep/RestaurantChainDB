from app import RestaurantDatabase


def search_product(restaurant_db, product_id):
    result = restaurant_db.search_product(product_id)
    if result:
        chain_name = result['chain_name']
        product_name = result['products'][0]['name']
        product_description = result['products'][0]['description']
        product_price = result['products'][0]['price']
        print(f"Product found in chain '{chain_name}':")
        print(f"Product Name: {product_name}")
        print(f"Description: {product_description}")
        print(f"Price: {product_price}")
    else:
        print("Product not found")


def display_detailed_information(restaurant_db, chain_name):
    # To Retrieve detailed information about a restaurant chain
    result = restaurant_db.restaurant_collection.find_one({'chain_name': chain_name})
    if result:
        print(f"Detailed Information for Restaurant Chain '{chain_name}':")
        print(f"Chain ID: {result['chain_id']}")
        print(f"Location: {result['location']}")
        print("Products:")
        for product in result['products']:
            print(f" - Product Name: {product['name']}")
            print(f"   Description: {product['description']}")
            print(f"   Price: {product['price']}")
    else:
        print(f"Restaurant Chain '{chain_name}' not found")


def display_detailed_product_information(restaurant_db, product_id):
    # Retrieve detailed information about a product
    result = restaurant_db.search_product(product_id)
    if result:
        chain_name = result['chain_name']
        product_name = result['products'][0]['name']
        product_description = result['products'][0]['description']
        product_price = result['products'][0]['price']
        print(f"Detailed Information for Product '{product_name}':")
        print(f"Product ID: {product_id}")
        print(f"Chain Name: {chain_name}")
        print(f"Description: {product_description}")
        print(f"Price: {product_price}")
    else:
        print(f"Product with ID '{product_id}' not found")


def main():
    DATA_FOLDER = 'data_folder'
    restaurant_db = RestaurantDatabase()

    # Load and insert data into MongoDB
    restaurant_db.load_data(DATA_FOLDER)

    print("**************** Welcome to the restaurant database! **********************")

    options = {
        '1': lambda: search_product(restaurant_db, input("Enter product ID: ")),
        '2': lambda: display_detailed_product_information(restaurant_db, input("Enter product ID: ")),
        '3': lambda: display_detailed_information(restaurant_db, input("Enter restaurant chain name: ")),
        '4': lambda: exit(),
    }

    while True:
        print("Options:")
        print("1. Search for products by product ID")
        print("2. Display detailed information about a product")
        print("3. Display detailed information about a restaurant chain")
        print("4. Exit")

        choice = input("Enter your choice: ")

        selected_option = options.get(choice)
        if selected_option:
            selected_option()
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
