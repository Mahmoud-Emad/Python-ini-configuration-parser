from configure.parser import ConfigParser
from errors.error import ErrorHandler

config = ConfigParser()
error = ErrorHandler()


def test_valid_section_name():
    """Test section name"""
    section = "section_name"
    assert error.validate_name(section)

    