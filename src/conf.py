__author__ = "Daniel Schneider"
__copyright__ = "Copyright 2022"
__credits__ = "Daniel Schneider"
__license__ = "Public"
__version__ = "1.0.0"
__maintainer__ = "Daniel Schneider"
__email__ = "xxx.xxx@xxx.xxx"
__status__ = "Develop"

import toml
import json

class DotDict(dict):
    """
    A class to parse a dictionary to dot-notation. This implementation supports nested dicts. \n
    Alternative implementation available: 
    from prodict import Prodict
    p = Prodict.from_dict(dictionary)

    usage: d = DotDict() or d = DotDict({'val1':'first'})
    set attributes: d.val2 = 'second' or d['val2'] = 'second'
    get attributes: d.val2 or d['val2']
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct):
        for key, value in dct.items():
            if hasattr(value, 'keys'):
                value = DotDict(value)
            self[key] = value


def load_toml(file='./cfg/settings.toml'):
    """Loads toml file

    Args:
        file (str, optional): absolute OML file to load. Defaults to './settings.toml'.

    Returns:
        dict: dot-notated dict
    """
    return DotDict(toml.load(file))


def load_json(file=''):
    """Loads json file

    Args:
        file (str, optional): _description_. Defaults to './cfg/settings.toml'.

    Returns:
        dict: dot-notated dict
    """
        
    file = open(file)
    return DotDict(json.load(file))
