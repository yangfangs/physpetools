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
The log configuration
"""

import logging
import os

from physpetool.utils.printstyle import print_style


def setlogdir(logdir):
    '''set the log directory'''
    # set log color
    logging.addLevelName(logging.INFO, print_style('%s', fore='green') % logging.getLevelName(logging.INFO))
    logging.addLevelName(logging.WARNING, print_style('%s', fore='red') % logging.getLevelName(logging.WARNING))
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
