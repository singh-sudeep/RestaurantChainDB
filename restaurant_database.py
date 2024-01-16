import os
import json
from pymongo import MongoClient


class RestaurantDatabase:
    DATA_FOLDER = 'data_folder'

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client['restaurant']
        self.restaurant_collection = self.db['restaurant_chain']
        self.menu_collection = self.db['menu']
    
    def save_data_to_db(self):
        pass

    def load_data_from_json(self):
        for filename in os.listdir(self.DATA_FOLDER):
            with open(os.path.join(self.DATA_FOLDER, filename), 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    if key == 'stores':
                        print(value)
                        break
                    break
                
                # read restaurant_name, location
                # create reasutauranchain object
                # read menu, attributessss
                # add menus in restauranthcain object add
            
                # Save to mongodb restaurnt_chain
                # save product informatioin in fproduction 
                # Save that file information in restauntarnt chain man

        print(file)
    
    def search_product(self, product_id):
        return 'product'

    def get_product_detail(self, product_id):

        return 'product_detail'