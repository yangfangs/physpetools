from physpetool.convert.concatenate import cocat_path
from physpetool.convert.fasta2phy import fasta2phy
from physpetool.phylotree.dogblocks import dogblocks
from physpetool.phylotree.domuscle import domuscle_file, domuscle
from physpetool.phylotree.doraxml import doraxml

# default arguments
raxmlpara_pro = "-f a -m PROTGAMMAJTTX  -p 12345 -x 12345 -# 100 -n T1"
raxmlpara_dna = "-f a -m GTRGAMMA  -p 12345 -x 12345 -# 100 -n T1"
musclepara = '-maxiters 100'
gblockspara_pro = '-t=p -e=-gb1'
gblockspara_dna = '-t=d -e=-gb1'



def build_hcp(in_put, out_put, args_muscle, args_gblocks, args_raxml, args_thread):
    '''reconstruct phylogenetic tree by hcp method'''
    out_retrieve = in_put
    out_alg = domuscle_file(out_retrieve, out_put, args_muscle)
    out_concat = cocat_path(out_alg)
    out_gblock = dogblocks(out_concat, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    doraxml(out_f2p, out_put, args_raxml, args_thread)


def build_srna(in_put, out_put, args_muscle, args_gblocks, args_raxml, args_thread):
    '''reconstruct phylogenetic tree by ssu rna method'''
    out_retrieve = in_put
    out_alg = domuscle(out_retrieve, out_put, args_muscle)
    if args_gblocks == gblockspara_pro:
        args_gblocks = gblockspara_dna
    out_gblock = dogblocks(out_alg, args_gblocks)
    out_f2p = fasta2phy(out_gblock)
    if args_raxml == raxmlpara_pro:
        args_raxml = raxmlpara_dna
    doraxml(out_f2p, out_put, args_raxml, args_thread)