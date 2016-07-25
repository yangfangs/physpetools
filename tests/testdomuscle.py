from physpetool.phylotree.domuscle import domuscle, domuscle_file

# test domuscle fuction
# input = "/home/yangfang/physpetools/testdata/protein.fastq"
# output = "/home/yangfang/physpetools/testdata/protein_alignment2.fasta"
# domuscle(input, output)

# test domuscle_file fuction
# input = "/home/yangfang/physpetools/testdata/temp/conserved_protein"
# output = "/home/yangfang/physpetools/testdata/phytree/test"
# out_alg = domuscle_file(input, output)
# print out_alg

musclepara = '-maxiters 100'
input = "/home/yangfang/physpetools/temp/16srnadata20160725152715"
output = "/home/yangfang/physpetools/testdata/test16srandata"
out_alg = domuscle(input, output,musclepara)
print out_alg