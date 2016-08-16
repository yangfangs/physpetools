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
