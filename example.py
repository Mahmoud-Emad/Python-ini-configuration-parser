from configure.parser import ConfigParser

config = ConfigParser()


config["section"] = {
    "key1":"this is a test value1",
    "key2":"this is a test value2"
}


config["newsection"] ={
    "domain_name":"example.com",
    "secretkey":"!@#$#$#@!!",
}

string_content = """
    [section]
    test=this is a test
    test2= this is a test2
    [newsection]
    Have= Yes
    Sure= No
"""

with open("example.ini", "w") as f:
    config.write(f) # Check example.ini file contents
    config.sections() # Return a list of sections
    config.get("newsection", "secretkey") # Get the value of a key in a section
    config.append('newsection', {'new':'new'}) # Append a new key/value pair to section 'newsection'
    config.append('section', {'new_test':'new_test'}) # Append a new key/value pair to section 'section'

'''
# Uncomment the following lines to test the read method if you have a file
with open("example.ini", "r") as f:
    config.read(f) # Read example.ini file contents | you must have file example.ini in the same directory
    config.read_from_string(string_content) # you can use this method to check if everything working well
    config.get("newsection", "Have") # Get the value of a key in a section
'''