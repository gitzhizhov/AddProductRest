import json


class Product:
    def __init__(self, name, type, exotic):
        self.name = name
        self.type = type
        self.exotic = exotic

    def get_dict(self):
        return self.__dict__
