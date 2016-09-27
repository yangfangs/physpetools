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
module return the time format dir

"""
import time


class timeformat:
    """The file add time format"""
    subdir = ''

    def __init__(self, sub):
        self.subdir = sub

    def __str__(self):
        time_format = '%Y%m%d%H%M%S'
        timeinfo = str(time.strftime(time_format))
        subdir = self.subdir + timeinfo
        return subdir


if __name__ == '__main__':
    doclu_subdir = timeformat('temp/hcp_alignment')
    print(doclu_subdir)
    print type(str(doclu_subdir))
