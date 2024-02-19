class RestaurantChain:
    def __init__(self, chain_name, location, phone_number,
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
                ):
        self.chain_name = chain_name
        self.location = location
        self.phone_number = phone_number
        self.type = type
        self.description = description
        self.local_hours = local_hours
        self.cuisines = cuisines
        self.food_photos = food_photos
        self.logo_photos = logo_photos
        self.store_photos = store_photos

        self.dollar_sign = dollar_sign
        self.pickup_enabled = pickup_enabled
        self.delivery_enabled = delivery_enabled
        self.offers_first_party_delivery = offers_first_party_delivery
        self.offers_third_party_delivery = offers_third_party_delivery

        self.weighted_rating_value = weighted_rating_value
        self.aggregated_rating_count = aggregated_rating_count
        self.supports_upc_codes = supports_upc_codes
        self.is_open = is_open
        self.menu_id = menu_id

        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def to_dict(self):
        return {
            'chain_name': self.chain_name,
            'location': self.location,
            'phone_number': self.phone_number,
            'type': self.type,
            'description': self.description,
            'local_hours': self.local_hours,
            'cuisines': self.cuisines,
            'food_photos': self.food_photos,
            'logo_photos': self.logo_photos,
            'store_photos': self.store_photos,
            'dollar_sign': self.dollar_sign,
            'pickup_enabled': self.pickup_enabled,
            'delivery_enabled': self.delivery_enabled,
            'offers_first_party_delivery': self.offers_first_party_delivery,
            'offers_third_party_delivery': self.offers_third_party_delivery,
            'weighted_rating_value': self.weighted_rating_value,
            'aggregated_rating_count': self.aggregated_rating_count,
            'supports_upc_codes': self.supports_upc_codes,
            'is_open': self.is_open,
            'menu_id': self.menu_id,
            'products': [product.product_id for product in self.products]
        }
