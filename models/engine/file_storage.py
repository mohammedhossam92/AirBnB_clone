import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:  # Use 'w' mode for writing text
            json.dump(self.__objects, f, default=self.obj_to_dict)

    def reload(self):
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


# Sample usage:
class SampleModel:
    def __init__(self, id):
        self.id = id

    def to_dict(self):
        return {'id': self.id}
