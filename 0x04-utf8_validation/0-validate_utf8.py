#!/usr/bin/python3
"""
The script contains a function to validate UTF8 encoding
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    :param:data list of integers
    :return: bool if the data is a valid utf8 encoding
    """

    num_byte = 0

    for byte in data:
        if num_byte == 0:
            if (byte >> 7) == 0:
                continue
            if (byte >> 5) == 0b110:
                num_byte = 1
            if (byte >> 4) == 0b1110:
                num_byte = 2
            if (byte >> 3) == 0b11110:
                num_byte = 3

        else:
            if (byte >> 6) != 0b10:
                return False

            num_byte -= 1

    return num_byte == 0
