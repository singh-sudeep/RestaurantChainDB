from pathlib import Path
from pymongo import MongoClient


class RestaurantDatabase:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['restaurant_db']
        self.restaurant_collection = self.db['restaurants']
        self.product_collection = self.db['products']

    def insert_product(self, product):
        product_doc = product.to_dict()
        self.product_collection.insert_one({
            'product_id': product_doc.get('product_id')
            'product_file': f"{product_doc('product_id')}.json"
        })

    def insert_restaurant_chain(self, restaurant_chain, product_folder_path):
        restaurant_doc = restaurant_chain.to_dict()
        restaurant_id = self.restaurant_collection.insert_one(restaurant_doc).inserted_id

        for product in restaurant_chain.products:
            product.save_to_file(product_folder_path)
            self.restaurant_collection.update_one(
                {'_id': restaurant_id},
                {'$addToSet': {'product_files': f'{product.product_id}.json'}}
            )
    
    def search_product(self, product_id):
        Home_Dir = Path.home()
        Product_Data_Dir = Path(r"OneDrive - Asia Pacific University\Desktop\ResturantChainDatabase\product_data")
        Product_Folder_Path = Home_Dir / Product_Data_Dir

        product = self.product_collection.find_one({'product_id': product_id})

        if product:
            product_file = f"{product_id}.json"
            product_path = Product_Folder_Path / Path(product_file)

            if product_path.exists():
                with open(str(product_path), 'r') as file:
                    product_data = file.read()
                return product, product_data
            else:
                return product, None
        else:
            return None, None
