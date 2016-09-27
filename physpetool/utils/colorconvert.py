# ########################## Copyrights and License #############################
#                                                                               #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                              #
#                                                                               #
# This file is part of PhySpeTree.                                              #
# https://xiaofeiyangyang.github.io/physpetools/                                #
#                                                                               #
# PhySpeTree is free software: you can redistribute it and/or modify it under   #
# the terms of the GNU Lesser General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)     #
# any later version.                                                            #
#                                                                               #
# PhySpeTree is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS     #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  #
# details.                                                                      #
#                                                                               #
# You should have received a copy of the GNU Lesser General Public License      #
# along with PhySpeTree. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                               #
# ###############################################################################

"""
Create random color value for color range used.

"""

import colorsys
import random

def convert(value):
    """
    convert 2------>16
    :param value: input int type
    :return: str type(16)
    """
    if value == 10:
        return "A"
    elif value == 11:
        return "B"
    elif value == 12:
        return "C"
    elif value == 13:
        return "D"
    elif value == 14:
        return "E"
    elif value == 15:
        return "F"
    return str(value)


def convert_hex(value):
    if value == "A":
        return str(10)
    elif value == "B":
        return str(11)
    elif value == "C":
        return str(12)
    elif value == "D":
        return str(13)
    elif value == "E":
        return str(14)
    elif value == "F":
        return str(15)
    return str(value)


def rgb2hex(rgb):
    """
    Convert RGB to HEX color
    :param rgb: Rge value example(23,32,44)
    :return: Hex value example #??????
    """
    hex = []
    for i in rgb:
        if i == 0:
            h = str(0) + str(0)
        else:
            h_left = i / 16
            h_right = i % 16
            h = convert(h_left) + convert(h_right)

        hex.append(h)
    hex_combine = "#" + ''.join(hex)
    return hex_combine


# #1722DF
def hex2rgb(hex_value):
    """
    Convert hex to rgp
    :param hex_value: string type example "#1722DF"
    :return: a rgb color tuple example (23,34,223)
    """
    hex = hex_value[1:]
    hex_splite = [convert_hex(x) for x in hex if x]
    hex_splite_rgb = splite_string(hex_splite, 2)
    rgb = [int(line[0]) * 16 + int(line[1]) for line in hex_splite_rgb if line]
    return tuple(rgb)


def splite_string(s, n):
    """ splite strings to sub"""
    return [s[i:i + n] for i in range(len(s)) if i % n == 0]


def rand_hsl():
    """
    Random hsl value
    :return: rgb_hsl value
    """
    h = random.uniform(0.02, 0.31) + random.choice([0, 1 / 3.0, 2 / 3.0])
    l = random.uniform(0.3, 0.8)
    s = random.uniform(0.3, 0.8)

    rgb = colorsys.hls_to_rgb(h, l, s)
    return (int(rgb[0] * 256), int(rgb[1] * 256), int(rgb[2] * 256))


def random_color(num):
    """
    get random color value
    :param num: int
    :return: a list contain Hex color value
    """
    color = []
    for i in range(num):
        color.append(rgb2hex(rand_hsl()))
    return color
