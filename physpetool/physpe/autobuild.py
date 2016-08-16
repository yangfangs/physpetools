import os
import subprocess
import sys

from physpetool.phylotree.domuscle import domuscle_file, domuscle
from physpetool.phylotree.dogblocks import dogblocks
from physpetool.phylotree.doraxml import doraxml
from physpetool.convert.fasta2phy import fasta2phy
from physpetool.convert.concatenate import cocat_path
from physpetool.phylotree.log import getLogging, setlogdir
from physpetool.phylotree.retrieve16srna import retrieve16srna
from physpetool.phylotree.retrieveprotein import doretrieve
import argparse

from physpetool.utils.checkinputfile import checkKeggOrganism, checkSilvaOrganism, checkFile

"""
the main module as enter point and contain a main() function to invoke other
script same as pipeline.
"""

APP_DESC = "construct"

raxmlpara_pro = "-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1"
raxmlpara_dna = "-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1"
musclepara = '-maxiters 100'
gblockspara_pro = '-t=p -e=-gb1'
gblockspara_dna = '-t=d -e=-gb1'


def start_args(input):
    """
Argument parse
    :param input: arguments
    """
    autobuild_args = input.add_argument_group("AUTOBUILD OPTIONS")
    advance_args = input.add_argument_group("ADVANCE OPTIONS")
    autobuild_args.add_argument('-i', nargs='?', dest='spenames', type=argparse.FileType('r'),
                                help='Input file must be contain the species names.')
    autobuild_args.add_argument('-o', action='store', dest="outdata",
                                default='Outdata', help='Out file name be string type.')
    autobuild_args.add_argument('-t', action='store', dest='thread',
                                type=int, default=1, help='Set the thread')
    autobuild_args.add_argument('-e', action='store', dest="extenddata",
                                help='The extended data should be FASTA format.')
    autobuild_args.add_argument('--hcp', action='store_true', dest='HCP',
                                default=False, help='Reconstruct phylogenetic tree by highly conserved proteins.')
    autobuild_args.add_argument('--ehcp', action='store_true', dest='EHCP',
                                default=False,
                                help='Reconstruct phylogenetic tree by highly conserved proteins and extended proteins.')
    autobuild_args.add_argument('--srna', action='store_true', dest='ssurna',
                                default=False, help='Reconstruct phylogenetic tree by 16s ssu ran.')
    autobuild_args.add_argument('--esrna', action='store_true', dest='essurna',
                                default=False,
                                help='Reconstruct phylogenetic tree by 16s ssu rna and extended 16s ssu rna.')
    autobuild_args.add_argument('-v', '--version', action='store_true',
                                default=False, help='Version information.')
    advance_args.add_argument('--muscle', action='store', dest='muscle',
                              default=musclepara, help='Alignment by muscle.')
    advance_args.add_argument('--gblocks', action='store', dest='gblocks',
                              default=gblockspara_pro, help='Use gblock.')
    advance_args.add_argument('--raxml', action='store', dest='raxml',
                              default=raxmlpara_pro, help='Build by raxml.')


def starting(args):
    """
starting run reconstruct tree
    :param args: arguments
    """
    print ("in put fasta file is:")
    print (args.spenames)
    print ("outfile is:")
    print (args.outdata + "\n")
    print ("now loading data and constructing species phylogenetic tree...")

    in_put = args.spenames

    pwd = os.getcwd()

    out_put = os.path.join(pwd, args.outdata)
    if args.extenddata:
        if os.path.isfile(args.extenddata):
            args_exted = args.exteddate
        elif os.path.isdir(args.extenddata):
            args_exted = os.path.join(pwd, args.extenddata)
    else:
        pass
    # reconstruct phylogenetic tree by highly conserved proteins
    if args.HCP:
        setlogdir(out_put)
        starting_hcp(in_put, out_put, args.muscle, args.gblocks, args.raxml, args.thread)
    # reconstruct phylogenetic tree by ssu RNA
    elif args.ssurna:
        setlogdir(out_put)
        starting_srna(in_put, out_put, args.muscle, args.gblocks, args.raxml, args.thread)
    elif args.EHCP:
        setlogdir(out_put)
        starting_ehcp(in_put, out_put, args.muscle, args.gblocks, args.raxml, args.thread, args_exted)

    elif args.essurna:
        setlogdir(out_put)
        starting_esrna(in_put, out_put, args.muscle, args.gblocks, args.raxml, args.thread, args_exted)


def starting_hcp(in_put, out_put, args_muscle, args_gblocks, args_raxml, args_thread):
    '''reconstruct phylogenetic tree by hcp method'''
    hcp_input = checkKeggOrganism(in_put)
    out_retrieve = doretrieve(hcp_input, out_put)
    out_alg = domuscle_file(out_retrieve, out_put, args_muscle)
    out_concat = cocat_path(out_alg)
    out_gblock = dogblocks(out_concat, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    doraxml(out_f2p, out_put, args_raxml, args_thread)


def starting_srna(in_put, out_put, args_muscle, args_gblocks, args_raxml, args_thread):
    '''reconstruct phylogenetic tree by ssu rna method'''
    ssu_input = checkSilvaOrganism(in_put)
    out_retrieve = retrieve16srna(ssu_input, out_put)
    out_alg = domuscle(out_retrieve, out_put, args_muscle)
    if args_gblocks is gblockspara_pro:
        args_gblocks = gblockspara_dna
        out_gblock = dogblocks(out_alg, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    if args_raxml is raxmlpara_pro:
        args_raxml = raxmlpara_dna
        doraxml(out_f2p, out_put, args_raxml, args_thread)


def starting_ehcp(in_put, out_put, args_muscle, args_gblocks, args_raxml, args_thread, args_exteddata):
    '''reconstruct phylogenetic tree by ehcp method'''
    hcp_input = checkKeggOrganism(in_put)
    out_retrieve = doretrieve(hcp_input, out_put)
    retrieve_pro = os.listdir(out_retrieve)
    for reline in retrieve_pro:
        fw_name = os.path.join(out_retrieve, reline)
        fr_name = os.path.join(args_exteddata, reline)
        fw = open(fw_name, 'ab')
        with open(fr_name) as fr:
            for line in fr:
                fw.write(line)
        fw.close()
    out_alg = domuscle_file(out_retrieve, out_put, args_muscle)
    out_concat = cocat_path(out_alg)
    out_gblock = dogblocks(out_concat, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    doraxml(out_f2p, out_put, args_raxml, args_thread)


def starting_esrna(in_put, out_put, args_muscle, args_gblocks, args_raxml, args_thread, args_extenddata):
    '''reconstruct phylogenetic tree by ssu rna extend method'''
    extend_check = checkFile(args_extenddata)
    ssu_input = checkSilvaOrganism(in_put)
    out_retrieve = retrieve16srna(ssu_input, out_put)
    retrieve_srna_path = os.path.join(out_retrieve, '16srandata.fasta')

    fw = open(retrieve_srna_path, 'ab')
    with open(extend_check) as read:
        for line in read:
            fw.write(line)
    fw.close()
    out_alg = domuscle(out_retrieve, out_put, args_muscle)
    if args_gblocks is gblockspara_pro:
        args_gblocks = gblockspara_dna
    out_gblock = dogblocks(out_alg, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    if args_raxml is raxmlpara_pro:
        args_raxml = raxmlpara_dna
    doraxml(out_f2p, out_put, args_raxml, args_thread)


def add_ehcp(data_path):
    pro_name = os.listdir(data_path)
