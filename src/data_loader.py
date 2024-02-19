import os
import json
from abc import ABC, abstractmethod


class DataLoader(ABC):
    @abstractmethod
    def load_data(self):
        pass


class JsonDataLoader(DataLoader):
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def load_data(self):
        data = []
        for filename in os.listdir(self.folder_path):
            with open(os.path.join(self.folder_path, filename), 'r') as file:
                restaurant_data = json.load(file)
                data.append(restaurant_data)
        return data


class DataLoaderFactory:
    @staticmethod
    def create_data_loader(data_type, folder_path):
        print(f"================> {folder_path} inside data Loader")
        if data_type == 'json':
            return JsonDataLoader(folder_path)
