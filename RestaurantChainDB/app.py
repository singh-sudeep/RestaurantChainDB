import os
import json
from pymongo import MongoClient


class RestaurantChain:
    def __init__(self, chain_id, chain_name, location):
        self.chain_id = chain_id
        self.chain_name = chain_name
        self.location = location
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def to_dict(self):
        return {
            'chain_id': self.chain_id,
            'chain_name': self.chain_name,
            'location': self.location,
            'products': [product.to_dict() for product in self.products]
        }


class Product:
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

    def save_to_file(self):
        filename = f'{self.product_id}.json'
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file)


class RestaurantDatabase:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['restaurant_db']
        self.restaurant_collection = self.db['restaurant']

    def insert_restaurant_chain(self, restaurant_chain):
        # To insert restaurant_chain document into MongoDB
        restaurant_doc = restaurant_chain.to_dict()
        self.restaurant_collection.insert_one(restaurant_doc)

    def search_product(self, product_id):
        # For searching product across different stores based on product_id
        return self.restaurant_collection.find_one({'products.product_id': product_id})

    def load_data(self, data_folder):
        for restaurant_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, restaurant_file), 'r') as file:
                data = json.load(file)
                chain_id = data.get('_id')
                chain_name = data.get('name')
                location = data.get('address')

                restaurant_chain = RestaurantChain(chain_id, chain_name, location)

                for menu in data.get('menus', []):
                    for category in menu.get('categories', []):
                        for menu_item in category.get('menu_item_list', []):
                            product = Product(
                                menu_item['product_id'],
                                menu_item['name'],
                                menu_item['description'],
                                menu_item.get('formatted_price', 0)
                            )
                            restaurant_chain.add_product(product)

                # To save product information as JSON files with product IDs as filenames
                for product in restaurant_chain.products:
                    product.save_to_file()

                # To Insert restaurant_chain document into MongoDB
                self.insert_restaurant_chain(restaurant_chain)


if __name__ == "__main__":
    data_folder_path = "data_folder"
    restaurant_db = RestaurantDatabase()

    # Load and insert data into MongoDB
    restaurant_db.load_data(data_folder_path)

    # Search for products by product ID
    product_id_to_search = "your_product_id"
    result = restaurant_db.search_product(product_id_to_search)

    if result:
        print(f"Product found: {result['products'][0]['name']}")
    else:
        print("Product not found")
