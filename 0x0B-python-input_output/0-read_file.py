#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """Prints and opens a file in read mode """
    with open("filename", encoding="utf-8") as f:
        print(f.read(), end="")
