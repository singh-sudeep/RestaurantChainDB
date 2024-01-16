from menu import Menu
from restaurantchain import RestaurantChain
from restaurant_database import RestaurantDatabase


def main():


    restaurantdb = RestaurantDatabase()
    restaurantdb.load_data_from_json()

    print("Welcome to the Resturant Database Management System")


    while True:
        print("1. Search Product")
        print("2. Get Product Detail")
        print("3: Exit")

        choice = int(input("Enter the operation you want to perform: "))

        if choice == 1:
            product_id = input("Enter the product_id to search: ")
            product = restaurantdb.search_product(product_id)

        if choice == 2:
            product_id = input("Enter the product_id to search: ")
            restaurantdb.get_product_details(product_id)

        if  choice == 3:
            break

    print('Good bye!')


if __name__ == "__main__":
    main()