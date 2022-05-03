"""
This package used to parse configuration files in the INI format.
"""
import re

class ErrorHandler:
    """Handler class for error messages and error checking."""
    @staticmethod
    def validate_name(name) -> str or NameError:
        """
        This methid takes a section name
        and and check if this name followed the right pattern.
        """
        string_check = re.compile(r'[@!#$%^&*()<>?/\|}{~: -]')
        if string_check.search(name):
            catch_name = string_check.findall(name)[0]
            index = name.index(catch_name)
            raise NameError(
                f'Name "{name}" is not valid, Try to remove "{catch_name}" at index {index}'
            )
        return "Valid"

    @staticmethod
    def validate_string(string) -> str or ValueError:
        """
        This method takes an ini string contant and check if it is valid.
        """
        section = None
        data = {}
        if string is None or string == "":
            raise ValueError("You can not write to an Empty/None string")
        if not isinstance(string, str):
            raise ValueError("The string is not a string")
        if string.split()[0][0] != "[" or string.split()[0][-1] != "]":
            raise ValueError("String section must start with [section]")
        for line in string.splitlines():
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1].upper()
                ErrorHandler.validate_name(section)
                data[section] = {}
            elif "=" in line:
                key, value = line.split("=")
                ErrorHandler.validate_name(key)
                key = key.replace(' ', '')
                data[section][key] = value
        return data

    @staticmethod
    def validate_reading_file(file_name):
        """Validate reading file_name"""
        with open(file_name, "r", encoding='utf-8') as file:
            line_no = 0
            for line in file:
                line_no += 1
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    section = line[1:-1]
                    ErrorHandler.validate_name(section)
                elif "=" in line:
                    key = line[0:line.index("=")]
                    ErrorHandler.validate_name(key)
                elif line == '':
                    continue
                else:
                    raise SyntaxError(f"Syntax Error at line {line_no}")
        return [file_name]
