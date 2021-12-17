#!/usr/bin/python3
"""
Print string
"""
def say_my_name(first_name, last_name=""):
   """Concatenate both parameters and print
   Parameters:
   first_name = first name
   last_name = last name
   Local Variables:
   fullname = empty string
   str_error1 = raise type error
   str_error2 = raise type error
   Return: None
   """
   fullname = ""
   str_error1 = "first_name must be a string"
   str_error2 = "last_name must be a string"
   if first_name and type(first_name) != str:
        raise TypeError(str_error1)
   elif first_name and type(first_name) == str:
        fullname += first_name + " "
   if last_name and type(last_name) != str:
        raise TypeError(str_error2)
   elif last_name and type(last_name) == str:
        fullname += last_name
   print("My name is {:s}".format(fullname))
