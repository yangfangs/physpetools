import os
from physpetool.database.dbpath import getlocaldbpath
from physpetool.utils.checkinputfile import checkFile, removeEmptyStr

dbpath = getlocaldbpath()


def colorRange(input, output, taxon):
    if not os.path.exists(output):
        os.path.makedirs(output)
    fw = open("range_color_by_kingdom",'ab')
    fw.write('TREE_COLORS\nSEPARATOR TAB\nDATA\n')
    inputfile = checkFile(input)
    if taxon == 'kingdom':
        organism_list = readTaxDb()
        input_list = readIputFile(inputfile)
        for line in input_list:
            for org in organism_list:
                if line == org:
                    write_data = "{0}\trang\t{1}\t{2}".format(line,color,anno)
                    fw.write(line +)





def readIputFile(inputfile):
    org_name =[]
    with open(inputfile) as f:
        for name in f:
            each_name = name.strip()
            org_name.append(each_name)

    org_name_check = removeEmptyStr(org_name)
    return org_name_check





def readTaxDb():
    orgpath = os.path.join(dbpath, "organism.txt")
    organism_list = []
    each_organism = []
    with open(orgpath) as f:
        for org in f:
            each_org = org.strip().split('\t')
            each_organism.append(each_org[0])
            each_organism.append(each_org[-1])
            organism_list.append(each_organism)
    return organism_list




def eachColorRange(taxon):
    if taxon == 'kingdom':
