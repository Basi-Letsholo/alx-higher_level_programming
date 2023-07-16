#!/usr/bin/python3
""" Square Class Module, inherits Rectangle. """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initialise Square attributes.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """ Retrieves size.
    """
    @property
    def size(self):
        return self.width

    """ Sets size of Square.
    """
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    """ Defines str repr of Square.
    """
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    """
    """
    def update(self, *args, **kwargs):
        if len(args) > 0:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i >= len(attr):
                    break
            setattr(self, attr[i], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)























