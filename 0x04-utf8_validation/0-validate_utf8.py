#!/usr/bin/python3
"""UTF-8 Validation
A function that determines if a given dataset represents a valid UTF-8 encoding
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the
 8 least significant bits of each integer
"""
from typing import List


def validUTF8(data: List) -> bool:
    """Return True if data is a valid UTF-8 encoding, else return False"""
    num_bytes = 0

    # loop through each integer in the data list
    for value in data:
        if num_bytes > 0:
            # check if first 2 bits are 10 which is a utf8 continuation byte
            if value >> 6 != 0b10:
                return False 
            else:
                num_bytes -= 1
        else:
            # check the first bit is 0: a 1-byte character
            if value >> 7 == 0:
                num_bytes = 0
            # check the first 3 bits is 110: 2-byte character
            elif value >> 5 == 0b110:
                num_bytes = 1
            # check the first 4 bits is 1110: 2-byte character
            elif value >> 4 == 0b1110:
                num_bytes = 2
            # check the first 5 bits is 11110: 2-byte character
            elif value >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
    return num_bytes == 0
