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
Module to call clustalw2 to do alignment

"""

#clustalw2 -INFILE=p1.fasta -TYPE=PROTEIN -OUTPUT=FASTA -ALIGN -OUTFILE=test/clustalw_p2.fasta
from physpetool.phylotree.log import getLogging

logdomuscle = getLogging('clutalw2')


def doclustalw_file(indata_files,outdata,clustalwpara):
    clustalwparas = clustalwpara.lstrip()
