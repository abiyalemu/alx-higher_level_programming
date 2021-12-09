#!/usr/bin/python3
class Square:
    """Class square"""

    def __init__(self, size=0):
        """Method to initiate"""
        self.size = size

    @property
    def size(self):
        """retreive size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """return square area"""
        return (self.__size**2)

    def my_print(self):
        """print to stdout square with char #"""
        if self.__size == 0:
            print()

        for k in range(self.__size):
            for l in range(self.__size):
                print('{}'.format('#'), end="")
            print()
