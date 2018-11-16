import os
os.chdir("/home/yangfang/PhySpeTree/updateSILVA/")
w_file = open('kegg_abb_to_ncbi_tax.txt','a')
with open('genome.txt') as f:
    for line in f:
        tem = line.strip().split(';')[0]
        tem2 = tem.split('\t')[1]
        tem3 = tem2.split(',')
        print(tem3)
        if len(tem3) == 2:
            w_file.write('{0}\t{1}\n'.format(tem3[0].strip(),tem3[1].strip()))
        else:
            w_file.write('{0}\t{1}\n'.format(tem3[0].strip(),tem3[2].strip()))
w_file.close()


#~~~~~~~~~~~~~~~~~~~~~~~~~~get all SILVA support orgnism~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
file_path = '/home/yangfang/PhySpeTree/updateSILVA/ftpfiles/'
all_pre_file = list(filter(lambda f: not f.startswith('.'), os.listdir(file_path)))
f_w = open('/home/yangfang/PhySpeTree/updateSILVA/support_srna_organism.txt','a')
for i in all_pre_file:
    f_w.write("{0}\n".format(i.strip().split('.')[0]))
f_w.close()