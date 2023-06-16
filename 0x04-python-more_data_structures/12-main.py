#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = 2
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XCV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XC"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CD"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CM"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
