from app import RestaurantDatabase


def search_product(product_id):
  product = RestaurantDatabase.products.find_one({'_id': product_id})
  if product:
    chain = RestaurantDatabase.chains.find_one({'_id': product['chain_id']})['name'] 
    print(f"Name: {product['name']}") 
    print(f"Description: {product['description']}")
    print(f"Price: {product['price']}")
    print(f"Chain: {chain}")
  else:
    print("Product not found")


def main():
    DATA_FOLDER = 'data_folder'
    restaurant_db = RestaurantDatabase()


    print("Welcome to the restaurant database!")
    while True:
        print("1. Search for products by product ID")
        print("2. Display detailed information about a product")
        print("3. Load Data")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            result = restaurant_db.search_product(product_id)
            print(result)

        elif choice == '2':
            break
        
        elif choice == '3':
          RestaurantDatabase.load_data(DATA_FOLDER)

    print('Goodbye!')


if __name__ == "__main__":
    main()
