import os
os.chdir('/home/yangfang/physpetools_data/TOF')

fw = open('ncbi_kegg_tol.txt', 'a')

with open('tol_tree.txt') as tol:
    for line in tol:
        strs = line.strip().split('\t')
        print (strs[1].strip())
        for abb in open('organism_convert_to_tax.txt'):
            abbs = abb.strip().split('\t')
            if strs[1].strip() == abbs[1].strip():
                result = abbs[0]
                # fw.write(strs[0] + '\t' + strs[1] +'\t' + result)
                # fw.write('\n')
                break

            else:
                result = 'NA'
        fw.write(strs[0] + '\t' + strs[1] +'\t' + result)
        fw.write('\n')
fw.close()