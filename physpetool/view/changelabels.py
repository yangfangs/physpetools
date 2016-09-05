import os

from physpetool.database.dbpath import getlocaldbpath
from physpetool.utils.checkinputfile import checkFile, readIputFile

dbpath = getlocaldbpath()


def taxlist():
    """
    prepare Taxonomy list
    :return: taxonomy list
    """
    orgpath = os.path.join(dbpath, "organism.txt")
    organism_list = []
    with open(orgpath) as f:
        for org in f:
            each_org = org.strip().split('\t')
            organism_list.append([each_org[1], each_org[2]])
    return organism_list


def annotatingLabels(input, output):
    """
Change labels
    :param input: input a files contain abb names
    :param output: output directory path
    :return: None
    """
    if not os.path.exists(output):
        os.makedirs(output)
    fw_name = "labels.txt"
    open_path = os.path.join(output, fw_name)
    fw = open(open_path, 'wb')
    fw.write('LABELS\nSEPARATOR TAB\nDATA\n')
    inputfile = checkFile(input)
    input_list = readIputFile(inputfile)
    tax_list = taxlist()
    for i in input_list:
        for j in tax_list:
            if i == j[0]:
                fw.write("{0}\t{1}".format(j[0], j[1]))
            else:
                pass
    fw.close()
    print("Change abbreviation names to full names complete")
    print("change labels file was save in {0}".format(open_path))