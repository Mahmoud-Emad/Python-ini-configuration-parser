from pyini_parser.configure.parser import ConfigParser
from pyini_parser.errors.error import ErrorHandler
import pytest



config = ConfigParser()
error = ErrorHandler()

string_content = """
    [section]
    test=this is a test
    test2=this is a test2
    [newsection]
    Have=Yes
    Sure=No
"""

def test_read_from_string():
    """Test read from string"""
    config.read_from_string(string_content)
    assert config.get("newsection", "Have") == "Yes"
    assert config.get("section", "test") == "this is a test"
    

def test_invalid_key():
    """Test invalid key"""
    config.read_from_string(string_content)
    with pytest.raises(KeyError):
        config.get("newsection", " Have")

def test_no_file():
    """Test no file"""
    file = None
    try:
        file = open("example.ini", "r")
    except FileNotFoundError:
        assert file == None

def test_read_file():
    """Test read file"""
    with open("example.ini", "a") as f:
        file = config.read(f)
        assert file == ['example.ini']
