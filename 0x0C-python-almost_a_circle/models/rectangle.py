#!/usr/bin/python3
"""Container with Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class that inherits from class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """Attr width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Attr height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X attr"""
        return self.__x

    @x.setter
    def x(self, value):
        """Settint x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y atrr"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """ __str__ method """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def to_dictionary(self):
        """Representation of Rectangle"""
        d = {"id": self.id, "width": self.__width, "height": self.__height,
             "x": self.__x, "y": self.__y}
        return d

    def update(self, *args, **kwargs):
        """Update with *args **kwargs"""
        attrs = ["id", "width", "height", "x", "y"]
        for elem in range(len(args)):
            for attr in range(len(attrs)):
                if attr == elem:
                    setattr(self, attrs[attr], args[elem])
                    break

        if not args or len(args) == 0:
            for key, val in kwargs.items():
                for attr in range(len(attrs)):
                    if key == attrs[attr]:
                        setattr(self, attrs[attr], val)
                        break

    def area(self):
        """Area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Representation of the rectangle with '#'"""
        for space in range(self.__y):
            print("")
        for row in range(self.__height):
            for move in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print("")
