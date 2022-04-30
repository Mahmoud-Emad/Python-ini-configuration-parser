## ini-configuration-parser

## description
<p>
    An INI file is a configuration file for computer software that consists of a text-based content with a structure and syntax comprising key–value pairs for properties, and sections that organize the properties.[1] The name of these configuration files comes from the filename extension INI, for initialization, used in the MS-DOS operating system which popularized this method of software configuration. The format has become an informal standard in many contexts of configuration, but many applications on other operating systems use different file name extensions, such as conf and cfg.
</p>

## Getting started
<p>Install the package</p>

```bash
$ pip install pyini-parser
```

```python

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
    config.append('devolvement', {'password':'#%$%80@#$36415'}) # Append a new key/value pair to section 'devolvement'
    config.read_from_string(string_content) # you can use this method to check if everything working well


# Uncomment the following lines to test the read method if you have a file
# config.read(f) # Read example.ini file contents | you must have file example.ini in the same directory

```

* Then you can test you'r file with pytest test library.

```bash
    $ pytest
```
You should see something like this
`======= 11 passed in 0.08s =======`
