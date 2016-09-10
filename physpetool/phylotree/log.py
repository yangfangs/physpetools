# ########################## Copyrights and License ############################
#                                                                              #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                             #
#                                                                              #
# This file is part of Physpe.                                                 #
# https://xiaofeiyangyang.github.io/physpetools/                               #
#                                                                              #
# Physpe is free software: you can redistribute it and/or modify it under      #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# Physpe is distributed in the hope that it will be useful, but WITHOUT ANY    #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with Physpe. If not, see <http://www.gnu.org/licenses/>.               #
#                                                                              #
# ##############################################################################

"""
The log configuration
"""


import logging
import os


def setlogdir(logdir):
    ldir = os.path.dirname(logdir)
    writelog = os.path.join(ldir, 'log.log')
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=writelog,
                        filemode='w')

    console = logging.StreamHandler()

    console.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')

    console.setFormatter(formatter)

    logging.getLogger('').addHandler(console)


def getLogging(name):
    return logging.getLogger(name)
