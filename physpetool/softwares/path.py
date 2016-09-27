
"""
The real path of software.
"""

import os
def getlocalpath():
    relpath = os.path.split(os.path.realpath(__file__))[0]
    return relpath