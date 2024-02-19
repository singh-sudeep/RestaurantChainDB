import uuid
from pathlib import Path
from restaurant_chain import RestaurantChain
from product import Product
from restaurant_database import RestaurantDatabase
from restaurant_cli import RestaurantCLI
from data_loader import DataLoaderFactory



def main():

    Home_Dir = Path.home()
    Sample_Data_Dir = Path(r"OneDrive - Asia Pacific University\Desktop\ResturantChainDatabase\sample_data")
    Product_Data_Dir = Path(r"OneDrive - Asia Pacific University\Desktop\ResturantChainDatabase\product_data")

    Data_Folder_Path = Home_Dir / Sample_Data_Dir
    Product_Folder_Path = Home_Dir / Product_Data_Dir
    data_type = 'json'

    data_loader = DataLoaderFactory.create_data_loader(data_type, str(Data_Folder_Path))
    restaurant_data = data_loader.load_data()

    database = RestaurantDatabase()
    
    for restaurant_info in restaurant_data:
        for data in restaurant_info.get('stores'):

            chain_name = data['name']
            location = data['address']
            phone_number = data['phone_number']
            type = data['type']
            description = data['description']
            local_hours = data['local_hours']
            cuisines = data['cuisines']
            food_photos = data['food_photos']
            logo_photos = data['logo_photos']
            store_photos = data['store_photos']

            dollar_sign = data['dollar_signs']
            pickup_enabled = data['pickup_enabled']
            delivery_enabled = data['delivery_enabled']
            offers_first_party_delivery = data['offers_first_party_delivery']
            offers_third_party_delivery = data['offers_third_party_delivery']

            weighted_rating_value = data.get('weighted_rating_value')
            aggregated_rating_count = data.get('aggregated_rating_count')
            supports_upc_codes = data.get('supports_upc_codes')
            is_open = data['is_open']
            menu_id = data['menu_id']
            menus = data['menus']

            restaurant_chain = RestaurantChain(
                chain_name,
                location,
                phone_number,
                type,
                description,
                local_hours,
                cuisines,
                food_photos,
                logo_photos,
                store_photos,
                dollar_sign,
                pickup_enabled,
                delivery_enabled,
                offers_first_party_delivery,
                offers_third_party_delivery,
                weighted_rating_value,
                aggregated_rating_count,
                supports_upc_codes,
                is_open,
                menu_id,
            )

            for menu in menus:
                for category in menu['categories']:
                    for product in category['menu_item_list']:

                        product_id = str(uuid.uuid4())
                        name = product['name']
                        description = product.get('description')
                        unit_size = product.get('unit_size')

                        unit_of_measurement = product.get('unit_of_measurement')
                        delivery_price = product.get('delivery_price')
                        delivery_min_price = product.get('delivery_min_price')
                        pickup_price = product.get('pickup_price')
                        pickup_min_price = product.get('pickup_min_price')
                        customizations = product.get('customizations')
                        formatted_price = product.get('formatted_price')
                        should_fetch_customizations = product.get('should_fetch_customizations')
                        supports_image_scaling = product.get('supports_image_scaling')

                        product = Product(
                            product_id,
                            name,
                            description,
                            unit_size,
                            unit_of_measurement,
                            delivery_price,
                            delivery_min_price,
                            pickup_price,
                            pickup_min_price,
                            customizations,
                            formatted_price,
                            should_fetch_customizations,
                            supports_image_scaling,
                            chain_name,
                        )

                        restaurant_chain.add_product(product)
                        database.insert_product(product)
            database.insert_restaurant_chain(restaurant_chain, Product_Folder_Path)

    cli = RestaurantCLI(database)
    cli.run()

if __name__ == "__main__":
    main()
