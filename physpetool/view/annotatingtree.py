# ########################## Copyrights and License ############################
#                                                                              #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                             #
#                                                                              #
# This file is part of PhyspeTree.                                             #
# https://xiaofeiyangyang.github.io/physpetools/                               #
#                                                                              #
# PhySpeTree is free software: you can redistribute it and/or modify it under  #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PhySpeTree is distributed in the hope that it will be useful, but WITHOUT ANY#
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PhySpeTree. If not, see <http://www.gnu.org/licenses/>.           #
#                                                                              #
# ##############################################################################

"""
Module for annotating tree.
"""

from physpetool.database.dbpath import getlocaldbpath
from physpetool.utils.checkinputfile import checkFile, readIputFile
from physpetool.utils.colorconvert import random_color
import os

dbpath = getlocaldbpath()

cite_range = u"""#==============================Color labels with ranges================================#
#                                                                                      #
# 1.This is a generated file by PhySpeTree.                                            #
#                                                                                      #
# 2.Users drop this file to iTOL account display the annotations.                      #
#                                                                                      #
# 3.iTOL V3: http://itol.embl.de/                                                      #
#                                                                                      #
# 4.Please cite:                                                                       #
#              Letunic, I., & Bork, P. (2016). Interactive tree of life (iTOL) v3:     #
#              an online tool for the display and annotation of phylogenetic and       #
#              other trees.Nucleic acids research, gkw290.                             #
#                                                                                      #
#======================================================================================#"""

cite_label = u"""#==============================Color labels without ranges=============================#
#                                                                                      #
# 1.This is a generated file by PhySpeTree.                                            #
#                                                                                      #
# 2.Users drop this file to iTOL account display the annotations.                      #
#                                                                                      #
# 3.iTOL V3: http://itol.embl.de/                                                      #
#                                                                                      #
# 4.Please cite:                                                                       #
#              Letunic, I., & Bork, P. (2016). Interactive tree of life (iTOL) v3:     #
#              an online tool for the display and annotation of phylogenetic and       #
#              other trees.Nucleic acids research, gkw290.                             #
#                                                                                      #
#======================================================================================#"""


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
    fw.write(cite_range)
    fw.write('\n')
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


def colorLabel(input, output, taxon):
    """
    Main function to color label
    :param input: input file names
    :param output: output directory path
    :param taxon: choice annotation by ['kingdom', 'phylum', 'class', 'order']
    :return: no
    """

    if not os.path.exists(output):
        os.makedirs(output)
    # writ file name
    fw_name = "labels_color_by_" + taxon + ".txt"
    open_path = os.path.join(output, fw_name)
    fw = open(open_path, 'wb')
    # write annotation range head
    fw.write(cite_label)
    fw.write('\n')
    fw.write('TREE_COLORS\nSEPARATOR TAB\nDATA\n')
    # check and get input list
    inputfile = checkFile(input)
    input_list = readIputFile(inputfile)
    # get match list and annotation dict to annotation
    match_list, anno_dict = matchInput(input_list, taxon)
    # write to annotation to file
    for line in match_list:
        color = anno_dict[line[1]]
        write_data = "{0}\tlabel\t{1}\n".format(line[0], color)
        fw.write(write_data)
    fw.close()
    print("Color labels by {0} was complete.".format(taxon))
    print("Color labels annotation was save in {0}".format(open_path))
