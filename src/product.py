from pathlib import Path
import json


class Product:
    def __init__(self,
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
                 chain_name
                ):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.unit_size = unit_size
        self.unit_of_measurement = unit_of_measurement
        self.delivery_price = delivery_price
        self.delivery_min_price = delivery_min_price
        self.pickup_price = pickup_price
        self.pickup_min_price = pickup_min_price
        self.customizations = customizations
        self.formatted_price = formatted_price
        self.should_fetch_customizations = should_fetch_customizations
        self.supports_image_scaling = supports_image_scaling
        self.chain_name = chain_name

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'unit_size': self.description,
            'unit_of_measurement': self.unit_of_measurement,
            'delivery_price': self.delivery_price,
            'delivery_min_price': self.delivery_min_price,
            'pickup_price': self.pickup_price,
            'pickup_min_price': self.pickup_min_price,
            'customizations': self.customizations,
            'formatted_price': self.formatted_price,
            'should_fetch_customizations': self.should_fetch_customizations,
            'supports_image_scaling': self.supports_image_scaling,
            'chain_name': self.chain_name,
        }
    
    def save_to_file(self, product_data_folder):
        filename_with_extension = Path(f'{self.product_id}.json')
        filename = str(product_data_folder / filename_with_extension)
        print("Fillllll========h>", filename)

        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file)
