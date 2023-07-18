#!/usr/bin/python3
""" Rectangle Tests module. """


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for Rectangle class.
    """

    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)
