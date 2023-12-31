#!/usr/bin/python3
"""importing modules"""
import cmd
import json
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNB that run the console module"""
    prompt = '(hbnb) '

    class_map = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def error_message(self, msg):
        """funtion to handle error"""
        print(f"{msg}")

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def get_instance(self, class_name, instance_id):
        """function to get the instance of the class"""
        key = f"{class_name}.{instance_id}"
        return storage.all().get(key)

    def execute_command(self, command, args):
        """function to excute commands"""
        commands = {
            "create": self.do_create,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "all": self.do_all,
            "update": self.do_update,
            "quit": self.do_quit,
            "EOF": self.do_EOF
        }

        if command in commands:
            commands[command](args)
        else:
            self.error_message("Invalid command")

    def do_quit(self, line):
        """function to quit"""
        return True

    def do_EOF(self, line):
        """function to exit """
        return True

    def do_create(self, line):
        """function to create new instance"""
        if not line:
            self.error_message("** class name missing **")
            return

        class_name = line.split()[0]
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        if class_name not in classes:
            self.error_message("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """function to show the data of the instance """
        if not line:
            self.error_message("** class name missing **")
            return

        args = line.split()
        class_name = args[0]
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        if class_name not in classes:
            self.error_message("** class doesn't exist **")
            return
        instance_id = args[1] if len(args) > 1 else None

        if not instance_id:
            self.error_message("** instance id missing **")
            return

        instance = self.get_instance(class_name, instance_id)

        if instance:
            print(instance)
        else:
            self.error_message("** no instance found **")

    def do_destroy(self, line):
        """file to destroy the instance"""
        if not line:
            self.error_message("** class name missing **")
            return

        args = line.split()
        class_name = args[0]
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        if class_name not in classes:
            self.error_message("** class doesn't exist **")
            return
        instance_id = args[1] if len(args) > 1 else None

        if not instance_id:
            self.error_message("** instance id missing **")
            return

        instance = self.get_instance(class_name, instance_id)

        if instance:
            key = f"{class_name}.{instance_id}"
            del storage.all()[key]
            storage.save()
        else:
            self.error_message("** no instance found **")

    def do_all(self, args):
        """function to show all the data"""
        # class_name = line.split()[0] if line else None
        # instances = storage.all().values()
        #
        # if class_name:
        #     instances = [instance for instance in instances
        #                  if instance.__class__.__name__ == class_name]
        #
        # print([str(instance) for instance in instances])
        if args and not HBNBCommand.class_map.get(args):
            print("** class doesn't exist **")
            return

        # result = {}
        # result.update(storage.all())
        if args:
            result = []
            for key, value in storage.all().items():
                if key.split(".")[0] == args:
                    result.append(str(value))
                    print(result)
        else:
            result = []
            for key, value in storage.all().items():
                result.append(str(value))
                print(result)

    def do_update(self, line):
        """function to update the instance"""
        if not line:
            print("** class name missing **")
            return

        args_list = line.split(" ")
        class_name = args_list[0]
        if not HBNBCommand.class_map.get(class_name):
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        instance = storage.all().get(
                class_name + "." + instance_id)
        if not instance:
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        instance_attribute = args_list[2]

        if len(args_list) < 4:
            print("** value missing **")
            return

        instance = self.get_instance(class_name, instance_id)
        instance_attribute_value: str = args_list[3]

        if instance:
            setattr(instance, instance_attribute, instance_attribute_value)
            instance.save()
        else:
            self.error_message("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
