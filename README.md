## INI-Configuration-file-parser

## description
<p>
    An INI file is a configuration file for computer software that consists of a text-based content with a structure and syntax comprising key–value pairs for properties, and sections that organize the properties.[1] The name of these configuration files comes from the filename extension INI, for initialization, used in the MS-DOS operating system which popularized this method of software configuration. The format has become an informal standard in many contexts of configuration, but many applications on other operating systems use different file name extensions, such as conf and cfg.
</p>

## Getting started
<p>Clone this repo and follow the steps below</p>

* You should install mypy for testing, or you can skip this step

```bash
    $ git clone Mahmoud-Emad/INI-Configuration-file-parser

    $ cd INI-Configuration-file-parser

    $ pip install mypy
```

```python

    from INI_Configuration_file_parser import ConfigParser


    config = ConfigParser()
    config['SectionName'] = {'key1': 'value1',
                    'key2': 'value2',
                    'key3': 'value3'}
    
    config['bitbucket.org'] = {'User': 'hg'}
    config['server'] = {'Host Port': '50022', 'User': 'hg', 'IdentityFile': '/home/hg/.ssh/id_rsa'}
    with open('test.ini', 'w') as configfile:
        config.write(configfile) // write the config to the file
        config.read('test.ini') // read the config from the file -> output will be in the terminal
        print(config.sections()) // output will be ['SectionName','bitbucket.org', 'server']
```

* Then you can test you'r file with mypy test library.

```bash
    $ mypy file_name.py
```
