from errors.error import ErrorHandler

from typing import Dict



class ConfigParser:
    def __init__(self):
        self.data = dict()
        self.view = dict()
        self.assert_error = ErrorHandler()
        self.filename = None
    
    def __str__(self):return self.data.__str__()
    def __exit__(self):self.close()

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
        with open(self.filename.name, "w") as f:
            for section in self.sections():
                self.assert_error.validate_name(section)
                f.write(f"[{section}]\n")
                for key, value in self.data[section].items():
                    self.assert_error.validate_name(key)
                    f.write(f"{key}={value}\n")
                f.write("\n")
        return f"{filename.name} written successfully"

    def get(self, section, key: str) -> str:
        """This method returns the value of the given key in the given section"""
        stander = self.data.get(section.upper()).get(key)
        if stander:
            return stander
        try:
            return self.view[section.upper()][key]
        except KeyError:
            raise KeyError(f"Key {key} not found in section {section}")

    def read_from_string(self, string: str) -> Dict:
        """This method reads the given string and returns a dictionary of sections and their values"""
        section = None
        for line in string.splitlines():
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1].upper()
                self.assert_error.validate_name(section)
                self.view[section] = dict()
            elif "=" in line:
                key, value = line.split("=")
                self.assert_error.validate_name(key)
                self.view[section][key] = value
        return self.view
    
    def read(self, filename) -> Dict:
        """This method reads the given file and returns a dictionary of sections and their values"""
        self.filename = filename
        with open(filename.name, "r") as f:
            return self.read_from_string(f.read())

    def append(self, section, items):
        """This method appends a new key/value pair to the given section"""
        self.data[section.upper()].update(items)
        return self.write(self.filename)
