from ini_parser.configure.parser import ConfigParser
from ini_parser.errors.error import ErrorHandler
import pytest, random


config = ConfigParser()


def test_valid_section_name():
    """Test section name"""
    section = "section_name"
    assert ErrorHandler.validate_name(section) == "Valid"

def test_invalid_section_name():
    """Test section name"""
    section = "section_name"
    with pytest.raises(NameError):
        ErrorHandler.validate_name(section.join('#'))
        ErrorHandler.validate_name(section.join('@'))
        ErrorHandler.validate_name(section.join('-'))
        ErrorHandler.validate_name(section.join(' '))

def test_get_sections():
    """Test get sections"""
    config.sections()
    assert config.sections() == []