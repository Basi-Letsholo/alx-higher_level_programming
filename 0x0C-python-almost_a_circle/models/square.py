#!/usr/bin/python3
""" Square Class Module, inherits Rectangle. """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class, inherits from rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialise attributes, inherited from Rectangle class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieves size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets size of Square.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """ Defines str repr of Square.
        """
        sq_str = '[Square] (' + str(self.id) + ') ' + str(self.x)
        sq_str = sq_str + '/' + str(self.y) + ' - ' + str(self.size)
        return sq_str

    def update(self, *args, **kwargs):
        """ Assigns attributes.
        """
        if len(args) > 0:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i >= len(attr):
                    break
            setattr(self, attr[i], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dictionary repr of Square.
        """
        sq_dict = {}
        sq_dict['id'] = self.id
        sq_dict['size'] = self.width
        sq_dict['x'] = self.x
        sq_dict['y'] = self.y

        return sq_dict
