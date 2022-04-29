from .exceptions import Error
import re


class ErrorHandler:
    """Handler class for error messages and error checking."""
    def validate_name(self, name) -> Error:
        """This methid takes a section name and and check if this name followed the right pattern."""
        string_check= re.compile('[@!#$%^&*()<>?/\|}{~: -]')
        if (string_check.search(name)):
            catch_name = string_check.findall(name)[0]
            index = name.index(catch_name)
            raise NameError(
                f'Name "{name}" is not valid, Try to remove "{catch_name}" at index {index}'
            )