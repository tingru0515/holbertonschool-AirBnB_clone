#!/usr/bin/python3
"""
This module provides HBNBCommand class inherited from cmd.Cmd class.
"""
import cmd

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.class_registry import find_class


class HBNBCommand(cmd.Cmd):
    """
    This class represents a command interpreter.

    Attributes:
        prompt (str): Prompt for the command line interface.
        storage_obj (FileStorage): Instance of FileStorage used for data storage.
        e_code (int): Error code for validation.
        ERROR_CODE (dict): Dictionary mapping error names to error codes.
    """

    prompt = "(hbnb) "
    storage_obj = FileStorage()
    e_code = 0
    ERROR_CODE = {
        "NO_NAME": 10,
        "NO_CLASS": 20,
        "NO_ID": 30,
        "NO_INSTANCE": 40,
        "NO_ATTRIBUTE": 50,
        "NO_VALUE": 60,
    }

    def split_arg_to_list(self, arg):
        """
        Splits the given string argument into a list.

        Args:
            arg (str): Input string to be split.

        Returns:
            List[str]: List of substrings.
        """

        return arg.split() if arg else []

    def initial_validator(self, args, layer=1):
        """
        Validates the arguments based on the specified layer.

        Args:
            args (List[str]): List of arguments to be validated.
            layer (int): Validation layer.

        Returns:
            int: Error code (0 if no error).
        """
        if not args:
            return HBNBCommand.ERROR_CODE["NO_NAME"]
        elif find_class(args[0]) == None and layer >= 2:
            return HBNBCommand.ERROR_CODE["NO_CLASS"]
        elif len(args) <= 1 and layer >= 3:
            return HBNBCommand.ERROR_CODE["NO_ID"]
        elif layer >= 4 and not self.find_instance(args[1]):
            return HBNBCommand.ERROR_CODE["NO_INSTANCE"]
        elif layer >= 5 and len(args) <= 2:
            return HBNBCommand.ERROR_CODE["NO_ATTRIBUTE"]
        elif layer >= 6 and len(args) <= 3:
            return HBNBCommand.ERROR_CODE["NO_VALUE"]
        return 0

    def error_printer(self, e_code):
        """
        Prints error messages based on the error code.

        Args:
            e_code (int): Error code.
        """
        if e_code == HBNBCommand.ERROR_CODE["NO_NAME"]:
            print("** class name missing **")
        elif e_code == HBNBCommand.ERROR_CODE["NO_CLASS"]:
            print("** class doesn't exist **")
        elif e_code == HBNBCommand.ERROR_CODE["NO_ID"]:
            print("** instance id missing **")
        elif e_code == HBNBCommand.ERROR_CODE["NO_INSTANCE"]:
            print("** no instance found **")
        elif e_code == HBNBCommand.ERROR_CODE["NO_ATTRIBUTE"]:
            print("** attribute name missing **")
        elif e_code == HBNBCommand.ERROR_CODE["NO_VALUE"]:
            print("** value missing **")

    def do_create(self, arg: str) -> None:
        """
        Command to create a new instance of BaseModel.

        Args:
            arg (str): Command argument.
        """
        args = self.split_arg_to_list(arg)
        HBNBCommand.e_code = self.initial_validator(args, 2)
        if not HBNBCommand.e_code:
            found_class = find_class(args[0])
            base_obj = found_class()
            HBNBCommand.storage_obj.save()
            print(base_obj.id)

    def find_instance(self, id):
        """
        Checks if an instance with the given ID exists.

        Args:
            id (str): ID to search for.

        Returns:
            bool: True if an instance with the ID exists, False otherwise.
        """
        all_objs = HBNBCommand.storage_obj.all()
        return any(obj.id == id for obj in all_objs.values())

    def do_show(self, arg: str) -> None:
        """
        Command to display information about a specified instance.

        Args:
            arg (str): Command argument.
        """
        args = self.split_arg_to_list(arg)
        HBNBCommand.e_code = self.initial_validator(args, 4)
        if not HBNBCommand.e_code:
            all_objs = HBNBCommand.storage_obj.all()
            obj = list(filter(lambda value: value.id ==
                       args[1], all_objs.values()))
            print(obj[0])

    def do_destroy(self, arg):
        """
        Command to delete a specified instance.

        Args:
            arg (str): Command argument containing instance ID.
        """
        args = self.split_arg_to_list(arg)
        HBNBCommand.e_code = self.initial_validator(args, 4)
        if not HBNBCommand.e_code:
            all_objs = HBNBCommand.storage_obj.all()
            for key in all_objs.keys():
                if all_objs[key].id == args[1]:
                    del all_objs[key]
                    FileStorage.objects == all_objs
                    HBNBCommand.storage_obj.save()
                    break

    def do_all(self, arg):
        """
        Command to display information about all instances.

        Args:
            arg (str): Command argument.
        """
        args = self.split_arg_to_list(arg)
        if not len(args):
            print(list(HBNBCommand.storage_obj.objects.values()))
            return
        HBNBCommand.e_code = self.initial_validator(args, 2)
        if not HBNBCommand.e_code:
            all_objs = list(
                val for val
                in HBNBCommand.storage_obj.all().values()
                if val.__class__.__name__ == args[0])
            print(all_objs)

    def do_update(self, arg):
        """
        Command to update attributes of a specified instance.

        Args:
            arg (str): Command argument containing instance ID, attribute, and value.
        """
        args = self.split_arg_to_list(arg)
        not_allowed_args = ["id", "created_at", "updated_at"]
        HBNBCommand.e_code = self.initial_validator(args, 6)
        if not HBNBCommand.e_code:
            all_objs = HBNBCommand.storage_obj.all()
            obj = list(filter(lambda value: value.id ==
                       args[1], all_objs.values()))[0]
            if args[2] not in not_allowed_args:
                # assume args[2] is valid arg
                key = obj.__class__.__name__ + "." + obj.id
                setattr(obj, args[2], args[3])
                all_objs[key] = obj
                FileStorage.objects == all_objs
                obj.save()

    def postcmd(self, stop, line):
        """
        Called after a command is executed. Handles error printing.

        Args:
            stop (bool): Boolean indicating whether to stop the command loop.
            line (str): Entered command line.

        Returns:
            bool: Value indicating whether to stop the command loop.
        """
        self.error_printer(HBNBCommand.e_code)
        HBNBCommand.e_code = 0
        return stop

    def do_quit(self, arg):
        """
        Command to exit the program.

        Args:
            arg (str): Command argument.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Command to exit the program on reaching the end of file.

        Args:
            arg (str): Command argument.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_help(self, arg):
        """
        Customized help command to display documented commands.

        Args:
            arg (str): Command argument.
        """
        print("\n")
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")

    def help_quit(self):
        """
        Called when an empty line is entered.
        """
        print("Quit command to exit the program\n")

    def help_EOF(self, arg):
        """EOF command to exit the program"""
        pass

    def emptyline(self):
        """Called when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
