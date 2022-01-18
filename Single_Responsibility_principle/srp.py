"""
Robert C Martin says:-
"Single Responsibility Principle: A class can have only one reason to change"

This means, a class should have only one task or functionality and where there is
change in that task/functionality, only then, that class should change.
"""

"""
Benefits of SRP:
1. When each class is following SRP then it is easy to maintain and undrestand.
2. Fewer bugs or defects in the code.
3. Testing and writing test classes is easier.
"""

# Example - Telephone Directory

from typing import Dict

# Primary task of this class is to:
# 1. add entry
# 2. delte entry
# 3. update entry
# 4. lookup for an entry
class TelephoneDirectory:
    def __init__(self):
        self.telephonedirectory = {}

    def add_entry(self, name, number) -> None:
        self.telephonedirectory[name] = number

    def delete_entry(self, name) -> None:
        self.telephonedirectory.pop(name)

    def update_entry(self, name, number) -> None:
        self.telephonedirectory[name] = number

    def lookup_entry(self, name) -> int:
        return self.telephonedirectory[name]

    def __str__(self):
        ret_dict = ""
        for key, value in self.telephonedirectory.items():
            ret_dict += f'{key} : {value}\n'
        return ret_dict

mytd = TelephoneDirectory()
mytd.add_entry("Virendar", 9645821)
mytd.add_entry("Raghav", 65845216)

mytd.delete_entry("Virendar")
mytd.update_entry("Raghav", 64582146)
print(mytd.lookup_entry("Raghav"))
print(mytd)

# Breaking Single Responsibility Principle
class TelephoneDirectory:
    def __init__(self):
        self.telephonedirectory = {}

    def add_entry(self, name, number) -> None:
        self.telephonedirectory[name] = number

    def delete_entry(self, name) -> None:
        self.telephonedirectory.pop(name)

    def update_entry(self, name, number) -> None:
        self.telephonedirectory[name] = number

    def lookup_entry(self, name) -> int:
        return self.telephonedirectory[name]

    ## these two methods should be in there own class
    def save_to_file(self, file_name, location):
        """
        this method saves the telephonedirectory data into
        a file at the given location
        """
        pass

    def save_to_database(self, database):
        """
        this file saves the telephonedirectory data into
        a database
        """
        pass

    def __str__(self):
        ret_dict = ""
        for key, value in self.telephonedirectory.items():
            ret_dict += f'{key} : {value}\n'
        return ret_dict


# Correcting SRP
# Divide the above class into smaller classes on the basis of there functionality
class TelephoneDirectory:
    def __init__(self):
        self.telephonedirectory = {}

    def add_entry(self, name, number) -> None:
        self.telephonedirectory[name] = number

    def delete_entry(self, name) -> None:
        self.telephonedirectory.pop(name)

    def update_entry(self, name, number) -> None:
        self.telephonedirectory[name] = number

    def lookup_entry(self, name) -> int:
        return self.telephonedirectory[name]

    def __str__(self):
        ret_dict = ""
        for key, value in self.telephonedirectory.items():
            ret_dict += f'{key} : {value}\n'
        return ret_dict

class Save_to_file:
    # functionality of class
    """
    save the objects to a file
    """
    def __init__(self, object_of_telephonedirectory):
        pass

class TelephoneDirecoryDB:
    #functionaliy of class
    """
    save the objects to database
    """
    def __init__(self, object_of_telephonedirectory) -> None:
        pass