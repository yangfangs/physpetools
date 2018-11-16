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
Create the kegg ko index database

"""
from urllib import request

from physpetool.tools.operateDB import operate_db

ko_db = operate_db('/home/yangfang/PhySpeTree/physpetools/physpetool/database/KEGG_DB_2.0.db')


def create_table_pro():
    """" create the table of highly conserved protein index"""
    table_name = "proindex"
    listko = []
    with open('/home/yangfang/PhySpeTree/physpetools/physpetool/database/protein_ko.txt') as org:
        for line in org:
            name = line.strip().split(',')
            listko.append(name[1])
    ko_db.create(table_name, listko)
    ko_db.dispay_col('proindex', 'NAME')


def insert_name():
    """insert the abb names"""
    orgs = []
    with open('/home/yangfang/PhySpeTree/physpetools/physpetool/database/organism.txt') as org:
        for line in org:
            strs = line.strip().split('\t')
            orgs.append(strs[1])
    ko_db.insert('proindex', orgs)


def get_abb():
    """Get the organism abb names"""
    euk = []
    prokar = []
    with open('/home/yangfang/PhySpeTree/physpetools/physpetool/database/organism.txt') as org:
        for line in org:
            strs = line.strip().split('\t')

            if strs[3].split(';')[0] == 'Eukaryotes':
                euk.append(strs[1])
            else:
                prokar.append(strs[1])
    return euk, prokar


def get_ko_list():
    """Gte eukaryotes and porkarytes KO list"""
    euk_ko = []
    prokar_ko = []
    with open('/home/yangfang/PhySpeTree/physpetools/physpetool/database/protein_ko.txt') as ko:
        for line in ko:
            strs = line.strip().split(',')
            euk_ko.append(strs[1])
            prokar_ko.append(strs[2])
    return euk_ko, prokar_ko


def getkolist(ko):
    """Get KO list"""
    listko = []
    url = "http://rest.kegg.jp/link/genes/" + ko

    page = request.urlopen(url).read()
    page = page.decode('utf-8')
    page = page.split('\n')
    page.remove('')
    for line in page:
        html = line.strip().split('\t')
        listko.append(html)
    return listko


def update_euk():
    '''Update eukaryote kegg protein index'''
    euk, prokar = get_abb()
    euk_ko, prokar_ko = get_ko_list()
    for line in euk_ko:
        kolist = getkolist(line)
        for ko in kolist:
            value = ko[1]
            list_abb = value.split(':')[0]
            if list_abb in euk:
                print('proindex', line, list_abb, value)
                ko_db.update('proindex', line, list_abb, value)


def update_prokar():
    """Update prokaryotes kegg protein index"""
    euk, prokar = get_abb()
    euk_ko, prokar_ko = get_ko_list()
    len_euk_ko = len(euk_ko)
    for line in range(len_euk_ko):
        kolist = getkolist(prokar_ko[line])
        for ko in kolist:
            value = ko[1]
            list_abb = value.split(':')[0]
            if list_abb in prokar:
                print('proindex', euk_ko[line], list_abb, value)
                ko_db.update('proindex', euk_ko[line], list_abb, value)


def display():
    ko_db.display_row('proindex', 'hsa')


if __name__ == '__main__':
    # Create table
    create_table_pro()
    # insert abb name
    insert_name()
    # Update eukaryotes protein index
    update_euk()
    # Update prokaryotes protein index
    update_prokar()
