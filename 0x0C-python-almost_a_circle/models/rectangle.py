#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation method
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): coordinate x
            y (int): coordinate y
            id (int)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width instance
        """
        return self.__width

    @property
    def height(self):
        """
        Getter for the height
        """
        return self.__height

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @width.setter
    def width(self, width):
        """
        Setter for width
        Args:
            width (int): width of the rectangle
        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """
        Setter for height
        Args:
            height (int): height of rectangle
        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """
        Setter for x
        Args:
            x (int): coordinate x
        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """
        Setter for y coordinate
        Args:
            y (int): coordinate y
        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Area of the rectangle
        Return:
            height * width
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle with '#'
        """
        width = self.width
        height = self.height
        for _ in range(self.y):
            print()
        for i in range(height):
            for _ in range(self.x):
                print(" ", end="")
            for j in range(width):
                print("#", end="")
            print()

    def __str__(self):
        """
        String representation of rectangle
        """
        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.__class__.__name__, self.id, self.x,
                self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        Args:
            *args : arguments to function
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif kwargs:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'width':
                    self.width = v
                if k == 'height':
                    self.height = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """
        Returns the dictionary representation of a rectangle
        Return:
            new_dict (dict): dictionary representation
        """
        new_dict = {}
        for k, v in self.__dict__.items():
            if k == 'id':
                new_dict['id'] = v
            if k == '_Rectangle__width':
                new_dict['width'] = v
            if k == '_Rectangle__height':
                new_dict['height'] = v
            if k == '_Rectangle__x':
                new_dict['x'] = v
            if k == '_Rectangle__y':
                new_dict['y'] = v
        return new_dict
