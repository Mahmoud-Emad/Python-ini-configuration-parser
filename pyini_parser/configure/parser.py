"""
This package used to parse configuration files in the INI format.
"""
from typing import Dict

from pyini_parser.errors.error import ErrorHandler



class ConfigParser:
    """
    ConfigParser class is used to parse configuration files in the INI format.
    """
    def __init__(self):
        self.data = {}
        self.view = {}
        self.filename = None

    def __str__(self):
        return self.data.__str__()

    def __getitem__(self, key):
        """Get the value of a key in a section"""
        return self.data.get(key)

    def __setitem__(self, section, items):
        """Set section value"""
        self.data[section.upper()] = items

    def sections(self):
        """This method returns a list of section names, in the order in which they were defined."""
        return list(self.data.keys())

    def write(self, filename) -> str:
        """This method writes the given file to the given filename"""
        self.filename = filename
        with open(self.filename.name, "w", encoding="utf-8") as file:
            for section in self.sections():
                ErrorHandler.validate_name(section)
                file.write(f"[{section}]\n")
                for key, value in self.data[section].items():
                    ErrorHandler.validate_name(key)
                    file.write(f"{key}={value}\n")
                file.write("\n")
        return f"{filename.name} written successfully"

    def get(self, section, key: str) -> str:
        """This method returns the value of the given key in the given section"""
        if len(self.data) > 0:
            stander = self.data.get(section.upper()).get(key)
            if stander:
                return stander
        try:
            return self.view[section.upper()][key]
        except KeyError:
            raise KeyError(f"Key {key} not found in section {section}") from KeyError

    def read_from_string(self, string: str) -> Dict:
        """
        This method reads the given string,
        and returns a dictionary of sections and their values
        """
        self.view = ErrorHandler.validate_string(string)
        return self.view

    def read(self, filename) -> Dict:
        """This method reads the given file and returns a dictionary of sections and their values"""
        self.filename = filename
        return ErrorHandler.validate_reading_file(self.filename.name)

    def append(self, section, items):
        """This method appends a new key/value pair to the given section"""
        if not isinstance(items, dict):
            raise TypeError("Items Must be a dictionary type")
        self.data[section.upper()].update(items)
        return self.write(self.filename)
