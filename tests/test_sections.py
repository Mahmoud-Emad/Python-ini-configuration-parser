from ini_configuration_parser.configure.parser import ConfigParser
from ini_configuration_parser.errors.error import ErrorHandler
import pytest, random


config = ConfigParser()
error = ErrorHandler()


def test_valid_section_name():
    """Test section name"""
    section = "section_name"
    assert error.validate_name(section) == "Valid"

def test_invalid_section_name():
    """Test section name"""
    section = "section_name"
    with pytest.raises(NameError):
        error.validate_name(section.join('#'))
        error.validate_name(section.join('@'))
        error.validate_name(section.join('-'))
        error.validate_name(section.join(' '))

def test_get_sections():
    """Test get sections"""
    config.sections()
    assert config.sections() == []