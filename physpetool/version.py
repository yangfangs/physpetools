version = '0.2.0'


VERSION_DESC = (
    """
          --------------------------------------------------------------------------------
                      Physpe (%s) - Reconstruct Phylogenetic Tree

          Citation: null

          --------------------------------------------------------------------------------
          """ % (version))


def version_infor():
    muscle_info = 'v3.8.31'
    gblocks_info = '0.91b'
    raxml_info = 'v8.2.3'
    author_info = 'Author: Yang Fang\n'
    print (VERSION_DESC)
    print (author_info)
    print ("Physpe call follow software if you use physpe please don't forget cite this:\n ")
    print ("============================CALL SOFTWARE INFO=============================================")
    print ('muscle version: '), (muscle_info + '\ncite:')
    print (citation['muscle'])
    print ('RAxML version: '), (raxml_info + '\ncite:')
    print (citation['RAxML'])
    print ('Gblocks version: '), (gblocks_info + '\ncite:')
    print (citation['Gblocks'])
    print ("===========================CALL SOFTWARE INFO==============================================")

citation = {
    'muscle': u"""Edgar R C. MUSCLE: multiple sequence alignment with high accuracy and
    high throughput[J]. Nucleic acids research, 2004, 32(5): 1792-1797.
    """,

    'RAxML': u"""Stamatakis A. RAxML version 8: a tool for phylogenetic analysis and
    post-analysis of large phylogenies[J]. Bioinformatics, 2014, 30(9): 1312-1313.
    """,

    'Gblocks': u"""Talavera G, Castresana J. Improvement of phylogenies after removing
    divergent and ambiguously aligned blocks from protein sequence alignments[J].
    Systematic biology, 2007, 56(4): 564-577.
    """
}

if __name__ == '__main__':
    version_infor()
