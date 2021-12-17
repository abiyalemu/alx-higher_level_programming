#!/usr/bin/python3
"""function  prints a text with 2 new lines after each\
   of these characters: ., ? and :
   Args:
        text: string
"""


def text_indentation(text):
    """Raises: TypeError if text isn't string
       Return: Nothing
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new = text.replace('.', '.\n\n')
    new = new.replace('?', '?\n\n')
    new = new.replace(':', ':\n\n')
    new = new.replace('\n\n ', '\n\n')
    print(new)
