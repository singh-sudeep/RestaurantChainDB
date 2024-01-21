import os
import json
from pprint import pprint 
from pymongo import MongoClient


class RestaurantChain:
    def __init__(self, chain_name, location):
        self.chain_name = chain_name
        self.location = location
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def to_dict(self):
        return {
            'chain_name': self.chain_name,
            'location': self.location,
            'product_ids': [product.product_id for product in self.products]
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
        restaurant_doc = restaurant_chain.to_dict()
        restaurant_id = self.restaurant_collection.insert_one(restaurant_doc).inserted_id

        for product in restaurant_chain.products:
            product.save_to_file()
            self.restaurant_collection.update_one(
                {'_id': restaurant_id},
                {'$addToSet': {'product_files': f'{product.product_id}.json'}}
            )
    
    def search_product(self, product_id):
        return self.product_collection.find_one({'product_id': product_id})

    @classmethod
    def load_data(cls, data_folder):
        for restaurant_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, restaurant_file), 'r') as file:
                data = json.load(file)
                stores = data.get('stores')
                for store_info in stores:
                    restaurant_chain = RestaurantChain(store_info['name'], store_info['address'])
                    for menu in store_info['menus']:
                            product = Product(
                                menu['product_id'],
                                menu['name'],
                                menu['description'],
                                menu['price']
                            )
                            restaurant_chain.add_product(product)
                    break
                cls.insert_restaurant_chain(restaurant_chain)
