'''check module'''
import os

from physpetool.phylotree.retrieveprotein import getcolname, getspecies, hcp_name
from physpetool.utils.checkinputfile import checkFile, readIputFile


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
    p = 0
    for line in match_ko:
        hcpname = hcp_name(line.strip())
        fw.write("'{0}' ----------------------------------> p{1}.fasta\n".format(hcpname, str(p)))
        p += 1
    fw.close()
