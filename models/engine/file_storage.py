#!/usr/bin/python3
"""importing models"""
import json
import os


class FileStorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all function to store all"""
        return self.__objects

    def new(self, obj):
        """new object added """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """save the data to the file json"""
        with open(self.__file_path, 'w') as f:  # Use 'w' mode for writing text
            json.dump(self.__objects, f, default=self.obj_to_dict)

    def reload(self):
        """reload data from the file"""
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    # Use 'r' mode for reading text
                    self.__objects = json.load(f)
        except Exception as e:
            print("Error reloading data:", e)

    def obj_to_dict(self, obj):
        """Convert object to a dictionary."""
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        return obj.__dict__
