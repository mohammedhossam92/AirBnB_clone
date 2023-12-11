#!/usr/bin/python3
"""importing models"""
import json
import os


class FileStorage:
    """file storage class"""
    # string -path to the json
    __file_path = "file.json"
    # dictionary - empty
    __objects = {}

    def all(self):
        """all function to store all"""
        return self.__objects

    def new(self, obj):
        """new object added """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save the data to the file json"""
        with open(self.__file_path, 'w') as f:  # Use 'w' mode for writing text
            json.dump(self.__objects, f, default=self.obj_to_dict)

    def reload(self):
        """reload function"""
        """importing modules to deal with """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        class_map = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        try:
            if not os.path.exists(FileStorage.__file_path):
                return
            with open(FileStorage.__file_path, 'r') as file:
                temporary_dict = {}
                temporary_dict = json.load(file)

                for key, value in temporary_dict.items():

                    # {
                    # string: {
                    # "key" : "value",  ==> value {"__class__": }
                    # }
                    #
                    # }
                    # string(key) = User(**value)  ==> construct user
                    # instance using **kwargs constructor
                    self.all()[key] = class_map[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def obj_to_dict(self, obj):
        """Convert object to a dictionary."""
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        return obj.__dict__


my_obj = FileStorage()
my_obj.save()