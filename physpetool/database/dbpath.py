
"""
Get the database real path.
"""

import os


def getlocaldbpath():
    relpath = os.path.split(os.path.realpath(__file__))[0]
    return relpath
