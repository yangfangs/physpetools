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
The module for check highly conserved proteins will be prepared.
"""


from physpetool.phylotree.retrieveprotein import getcolname, getspecies, hcp_name
from physpetool.utils.checkinputfile import checkFile, readIputFile
import os


def check_ehcp(input, output):
    if not os.path.exists(output):
        os.makedirs(output)
    fw_name = "physpe_echp_extend.txt"
    open_path = os.path.join(output, fw_name)
    fw = open(open_path, 'wb')

    input_path = checkFile(input)
    input_list = readIputFile(input_path)
    colname = getcolname()
    relist, match_ko = getspecies(input_list, colname)
    p = 1
    for line in match_ko:
        hcpname = hcp_name(line.strip())
        massage = "'{0}' ----------------------------------> p{1}.fasta\n".format(hcpname, str(p))
        print(massage)
        fw.write(massage)
        p += 1
    print("Check extend highly conserved protein is completed.\n")
    print("Check result is store in {0}".format(open_path))
    fw.close()
