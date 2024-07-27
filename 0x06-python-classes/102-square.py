#!/usr/bin/python3
'''The square Module'''


class Square:
    '''The Square class'''
    def validator(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        '''Constructor
        Args:
            size: Size of an square instance
        '''
        self.size = size

    @property
    def size(self):
        '''Getter for size attribute'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter for size attribute'''
        self.validator(value)
        self.__size = value

    def area(self):
        '''Method to get are of a square'''
        return self.__size * self.__size

    def __eq__(self, other):
        '''Equality dunder method'''
        if isinstance(other, Square):
            return self.size == other.size

    def __nq__(self, other):
        '''Inequality dunder method'''
        if isinstance(other, Square):
            return self.size != other.size

    def __lt__(self, other):
        '''Less than dunder method'''
        if isinstance(other, Square):
            return self.size < other.size

    def __gt__(self, other):
        '''Greater than dunder method'''
        if isinstance(other, Square):
            return self.size > other.size

    def __ge__(self, other):
        '''Greater than or equal dunder method'''
        if isinstance(other, Square):
            return self.size >= other.size

    def __le__(self, other):
        '''Less than or equal dunder method'''
        if isinstance(other, Square):
            return self.size <= other.size
