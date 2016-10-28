from physpetool.phylotree.retrievessurna import retrieve16srna

lst = ['aaa', 'hsa', 'aac', 'aad']
outpath = '/home/yangfang/physpetools/testdata'
pahts = retrieve16srna(lst, outpath)
print pahts