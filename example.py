from pyini_parser.configure.parser import ConfigParser

config = ConfigParser()

config["deployment"] = {
    "domain_name": "www.example.com",
    "secret_key": "!@#$#$#@!!",
}

config["database"] = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
}
config["email"] = {
    "host": "smtp.gmail.com",
    "port": "587",
}
config["devolvement"] = {
    "api_key": "!@#$%^&*()_+",
}
string_content = """
    [deployment]
    domain_name=www.example.com
    secret_key=!@#$#$#@!!
    [devolvement]
    api_key=!@#$%^&*()_+
"""

with open("example.ini", "w") as f:
    config.write(f) # Check example.ini file contents
    config.sections() # Return a list of sections
    config.get("deployment", "domain_name") # Get the value of a key in a section
    config.append('devolvement', {'password':'#%$%80@#$36415'}) # Append a new key/value pair to section 'newsection'
    print(config.read_from_string(string_content))

'''
# Uncomment the following lines to test the read method if you have a file
with open("example.ini", "r") as f:
    config.read(f) # Read example.ini file contents | you must have file example.ini in the same directory
    config.read_from_string(string_content) # you can use this method to check if everything working well
    config.get("section", "key") # Get the value of a key in a section
'''