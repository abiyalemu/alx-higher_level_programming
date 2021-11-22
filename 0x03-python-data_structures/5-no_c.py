#!/usr/bin/python3
def no_c(my_string):
    new_string = (''.join(k for k in my_string if k != 'c' and k != 'C'))
    return new_string
