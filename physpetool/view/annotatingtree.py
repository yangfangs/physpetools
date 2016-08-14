import os
from physpetool.database.dbpath import getlocaldbpath
from physpetool.utils.checkinputfile import checkFile, removeEmptyStr
from physpetool.utils.colorconvert import random_color

dbpath = getlocaldbpath()


def readIputFile(inputfile):
    """
    prepare and check input file list
    :param inputfile:
    :return: inputfile by check list
    """
    org_name = []
    with open(inputfile) as f:
        for name in f:
            each_name = name.strip()
            org_name.append(each_name)

    org_name_check = removeEmptyStr(org_name)
    return org_name_check


def readTaxDb():
    """
    prepare Taxonomy list
    :return: taxonomy list
    """
    orgpath = os.path.join(dbpath, "organism.txt")
    organism_list = []
    with open(orgpath) as f:
        for org in f:
            each_org = org.strip().split('\t')
            organism_list.append([each_org[1], each_org[-1]])
    return organism_list


def matchInput(input_organism, taxon):
    """
    Match input file with DB
    :param input_organism: input
    :param taxon:
    :return: a match list and annotation dict use annotation
    """
    organism_list = readTaxDb()
    # choice range
    taxon_dict = {'kingdom': 0, 'phylum': 1, 'class': 2, 'order': 3}
    id = taxon_dict.get(taxon)
    match_list = []
    anno = []
    for i in input_organism:
        for j in organism_list:
            if i == j[0]:
                temp_anno = j[1].split(';')[id].strip()
                anno.append(j[1].split(';')[id].strip())
                match_list.append([i, temp_anno])
                break
            else:
                pass
    # check annotation number
    unique_anno = list(set(anno))
    length_anno = len(unique_anno)
    # get random color
    color = random_color(length_anno)
    anno_dict = {}
    # get a annotation dict {'plants':'#77E9CC'}
    for line in range(length_anno):
        anno_dict[unique_anno[line]] = color[line]
    return match_list, anno_dict


def colorRange(input, output, taxon):
    """
    Main function to color range
    :param input: input file names
    :param output: output directory path
    :param taxon: choice annotation by ['kingdom', 'phylum', 'class', 'order']
    :return: no
    """
    if not os.path.exists(output):
        os.makedirs(output)
    # writ file name
    fw_name = "range_color_by_" + taxon + ".txt"
    open_path = os.path.join(output, fw_name)
    fw = open(open_path, 'wb')
    # write annotation range head
    fw.write('TREE_COLORS\nSEPARATOR TAB\nDATA\n')
    # check and get input list
    inputfile = checkFile(input)
    input_list = readIputFile(inputfile)
    # get match list and annotation dict to annotation
    match_list, anno_dict = matchInput(input_list, taxon)
    # write to annotation to file
    for line in match_list:
        color = anno_dict[line[1]]
        write_data = "{0}\trange\t{1}\t{2}\n".format(line[0], color, line[1])
        fw.write(write_data)
    fw.close()
    print("Color range by {0} was complete.".format(taxon))
    print("Color range annotation was save in {0}".format(open_path))
