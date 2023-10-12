from typing import *



def dataTypes(type: str):
    if type == "Integer":
        print('4')
    elif type == "Long":
        print('8')
    elif type == "Float":
        print('4')
    elif type == "Double":
        print('8')
    else :
        print('1')
    return

a= str(input())
dataTypes(a)