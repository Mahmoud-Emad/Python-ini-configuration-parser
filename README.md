## ini-configuration-parser

## description
<p>
    An INI file is a configuration file for computer software that consists of a text-based content with a structure and syntax comprising key–value pairs for properties, and sections that organize the properties.[1] The name of these configuration files comes from the filename extension INI, for initialization, used in the MS-DOS operating system which popularized this method of software configuration. The format has become an informal standard in many contexts of configuration, but many applications on other operating systems use different file name extensions, such as conf and cfg.
</p>

## Getting started
<p>Clone this repo and follow the steps below</p>

* You should install pytest for testing, or you can skip this step

```bash
    $ git clone Mahmoud-Emad/ini-configuration-parser

    $ cd ini-configuration-parser

    $ pip install pytest
```

```python

from configure.parser import ConfigParser

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

'''
# Uncomment the following lines to test the read method if you have a file
with open("example.ini", "r") as f:
    config.read(f) # Read example.ini file contents | you must have file example.ini in the same directory
    config.read_from_string(string_content) # you can use this method to check if everything working well
    config.get("section", "key") # Get the value of a key in a section
'''
```

* Then you can test you'r file with mypy test library.

```bash
    $ pytest
```
