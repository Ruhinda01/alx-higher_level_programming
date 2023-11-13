#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits fro rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiation method
        Args:
            size (int): size of square
            x (int): coordinate x axis
            y (int): coordinate y axis
            id (int): id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String represntation of square
        """
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter for size
        """
        return self.height

    @size.setter
    def size(self, value):
        """
        Setter for square
        Args:
            value (int): size of the square
        Raises:
            TypeError: value must be an integer
            ValueError: value must be > 0
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        Args:
            *args : arguments to function
            **kwargs: can be thought as a double pointer to dict
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        elif kwargs:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """
        Returns the dictionary representation of a square
        Return:
            new_dict (dictionary): a new dictionary rep
        """
        new_dict = {}
        for k, v in self.__dict__.items():
            if k == 'id':
                new_dict['id'] = v
            if k == '_Rectangle__width' or k == '_Rectangle__height':
                new_dict['size'] = v
            if k == '_Rectangle__x':
                new_dict['x'] = v
            if k == '_Rectangle__y':
                new_dict['y'] = v
        return new_dict
