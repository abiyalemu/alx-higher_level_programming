#!/usr/bin/python3
"""Square class documentation"""


class Square():
    """A quadrilateral with four equal sides to square class"""

    def __init__(self, size=0):
        """Sets the initial size value upon instantiation of the class
           Throws errors if the value passed in is not an integer
        Args:
            size (int, optional): the size of the square object
        Raises:
            TypeError: The value passed in is not an integer
            ValueError: The value passed in is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square"""     
        return self.__size**2
