class RestaurantChain:
    def __init__(self, chain_name, location):
        self.chain_name = chain_name
        self.location = location
        self.menus = []
    
    def add_item_in_menu(self, menu):
        self.menus.append(menu)
    
    def to_dict(self):
        return {
            'chain_name': self.chain_name,
            'location': self.location,
            'menus': [menu.to_dict() for menu in self.menus]
        }
