#!/usr/bin/python3
"""
This is the AirBnB command interface for the AirBnB project that
inherits from the cmd class
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.__init__ import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    An instance HBNBCommand

    Attributes:
        intro: a message to welcome the user
        prompt: The text issued on every cmd instance
        __classes - Contains a dictionary of all classes
    """
    prompt = "(hbnb) "
    __classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }

    __types = {
                "age": int, "number_rooms": int, "number_bathrooms": int,
                "max_guest": int, "price_by_night": int,
                "latitude": float, "longitude": float
            }

    def do_create(self, line):
        """
        create an instance of a class

        Args:
            line (str)- class name, parsed directly from the cmd-line
        """
        if len(line) == 0:
            print('** class name missing **')
        elif line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_model = HBNBCommand.__classes[line]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id

        Args:
            line (str)- class name, parsed directly from the cmd-line
        Raises:
            An exception is raised is line is empty or if className does not
            exist or if id is not present
        """
        args = line.split()

        try:
            className = args[0]
            if className not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except Exception as e:
            print("** class name missing **")
            return

        try:
            id = args[1]
        except Exception as e:
            print('** instance id missing **')
            return

        key = className + "." + str(id)
        fetch_dicts = storage.all()
        try:
            print(fetch_dicts[key])
        except Exception as e:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)

        Args:
            line (str)- class name, parsed directly from the cmd-line
        Raises:
            An exception is raised is line is empty or if className does not
            exist or if id is not present
        """
        args = line.split()

        try:
            className = args[0]
            if className not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except Exception as e:
            print("** class name missing **")
            return

        try:
            id = args[1]
        except Exception as e:
            print('** instance id missing **')
            return

        key = className + "." + str(id)
        fetch_dicts = storage.all()

        try:
            del(fetch_dicts[key])
            storage.save()
        except Exception as e:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name.

        Args:
            line (str)- class name, parsed directly from the cmd-line
        """
        objects = storage.all()
        objects_list = []

        if not line:
            print("** class doesn't exist **")
        else:
            if line not in HBNBCommand.__classes:
                print("** class name missing **")
            else:
                for key, obj_val in objects.items():
                    if line in key:
                        objects_list.append(str(obj_val))
                print(objects_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)

        Args:
            line (str)- class name, parsed directly from the cmd-line
        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        Rules:
            Only one attribute can be updated at the time
        Raises:
            An exception is raised is line is empty or if className does not
            exist or if id is not present
        """
        args = line.split()

        try:
            className = args[0]
            if className not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
        except Exception as e:
            print("** class name missing **")
            return

        try:
            id = args[1]
        except Exception as e:
            print('** instance id missing **')
            return

        try:
            attribute = args[2]
        except Exception as e:
            print('** attribute name missing **')
            return

        try:
            value = args[3]
            # Properly parse the value
            if "\"" in value:
                value = value[1:-1]
            elif attribute in HBNBCommand.__types:
                value = HBNBCommand.__types[attribute](value)
            else:
                value = value
        except Exception as e:
            print('** value missing **')
            return

        key = className + "." + str(id)
        fetch_dicts = storage.all()

        try:
            target = fetch_dicts[key]
            setattr(target, attribute, value)
            target.save()
        except Exception as e:
            print("** no instance found **")

    def do_count(self, line):
        """
        Returns the count of the parsed in class instance created

        Args:
            line (str)- class name, parsed directly from the cmd-line
        """
        objects = storage.all()
        objects_list = []

        if not line:
            print("** class doesn't exist **")
        else:
            if line not in HBNBCommand.__classes:
                print("** class name missing **")
            else:
                for key, obj_val in objects.items():
                    if line in key:
                        objects_list.append(str(obj_val))
                print(len(objects_list))

    def precmd(self, line):
        """
        pre command line function that process every args before being
        parsed

        Args:
            line (str)- class name, parsed directly from the cmd-line
        """
        arg = ''
        if '.' in line.split()[0]:
            res = line.split('.')
            if res[1][-1] == ')' and res[1][-2] == '(':
                arg = res[1][:-2] + ' ' + res[0]
            elif res[1][-1] == ')' and res[1][-2] == '}':
                entry = res[1][:-1].split('(')
                content = entry[1].split(',')
                obj = content[1][1:].split(':')
                arg = (
                    entry[0] + ' ' + res[0] + ' ' + content[0][1:-1] +
                    ' ' + obj[0][2:-1] + '' + obj[1]
                )
            elif res[1][-1] == ')' and (
                    res[1][-2] == '"' or res[1][-2] != '"'
                    ):
                entry = res[1][:-1].split('(')
                if entry[0] == 'update':
                    content = entry[1].split(',')
                    arg = (
                        entry[0] + ' ' + res[0] + ' ' + content[0][1:-1] +
                        ' ' + content[1][2:-1] + '' + content[2]
                    )
                else:
                    arg = entry[0] + ' ' + res[0] + ' ' + entry[1][1:-1]
            else:
                arg = res[1] + ' ' + res[0]
        else:
            arg = line

        return arg

    def emptyline(self):
        """
        emptyline - This method called when we have an empty line.
                    If this method is not overridden,
                    it repeats the last nonempty command entered.
        """
        pass

    def do_quit(self, line):
        """a function that ends the program interaction\n"""
        print("Exit command to leave program")
        print()
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program.\n"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
