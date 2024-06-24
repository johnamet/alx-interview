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

    for i in data:
        if i > 0 and i < 127:
            continue
        else:
            return False
    return True
