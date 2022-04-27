from typing import Dict


class ConfigParser:
    def __init__(self):
        self._sections = dict()
    
    def __str__(self):return f"{self._sections}"
    
    def __getitem__(self, key):
        """Get the value of a key in a section"""
        return self._sections.get(key)
    
    def __setitem__(self, key, value):
        """Set section value"""
        self._sections[key] = value
    
    def sections(self):
        """This method returns a list of section names, in the order in which they were defined."""
        return list(self._sections.keys())

    def write(self, filename):
        """This method writes the given file to the given filename"""
        with open(filename.name, "w") as f:
            for section, values in self._sections.items():
                if " " in section:
                    raise ValueError("Section names cannot contain spaces")
                f.write(f"[{section.upper()}]\n")
                for key, value in values.items():
                    f.write(f"{key.upper().strip()}={value}\n")

    def read(self, filename):
        """This method reads the given file and returns a dictionary of sections and their values"""
        output = dict()
        with open(filename.name, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    section = line[1:-1]
                    output[section] = dict()
                elif "=" in line:
                    key, value = line.split("=")
                    output[section][key] = value
        return output