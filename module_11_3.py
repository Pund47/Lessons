import sys
from pprint import pprint

def introspection_info(obj):
    list = {}
    list['type'] = type(obj)
    list['atribute'] = dir(obj)

    list['place']  = sys.path
    #list.append(
    return list

number_info = introspection_info(42)
pprint(number_info)