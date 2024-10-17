import inspect
import sys
from pprint import pprint

def introspection_info(obj):
list = {}
list['type'] = type(obj)
list['atribute'] = dir(obj)
list['module'] = inspect.getmodule(obj)
list['metods'] = inspect.getmembers(obj)
list['module_of_call'] = obj.__ne__
list['place'] = sys.path
return list

number_info = introspection_info(42)
pprint(number_info)
