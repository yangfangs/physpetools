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
