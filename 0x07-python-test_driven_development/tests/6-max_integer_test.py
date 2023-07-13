#!/usr/bin/python3
""" Max int Test module. """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """
    Test cases for max int function.
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 4, 3, 1]), 4)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-9, -12, -5, -234]), -5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([4, 2, 1]), 4)

        with self.assertRaises(TypeError):
            max_integer(3)
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3])
