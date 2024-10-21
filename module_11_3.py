import inspect
import sys
from pprint import pprint

def introspection_info(obj):
    my_list = {}
    list_callable = []
    list_no_callable = []
    my_list['type'] = type(obj)
    all_met = dir(obj)
    for i in all_met:
        if callable(getattr(obj,i)) == True:
            list_callable.append(i)
        else:
            list_no_callable.append(i)
    my_list['atribute'] = list_no_callable #не вызываемый
    my_list['metods'] = list_callable  #вызываемый
    my_list['module'] = inspect.getmodule(obj)
    my_list['module_of_call'] = getattr(obj,"__module__","Не имеет модуль.")

    try:
        my_list['place'] = inspect.getfile(obj)
    except TypeError:
        my_list['place'] = "Файл не определен или объект встроенный"

    return my_list

number_info = introspection_info(42)
pprint(number_info)
