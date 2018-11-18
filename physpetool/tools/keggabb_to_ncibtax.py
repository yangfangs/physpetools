import os

os.chdir("/home/yangfang/PhySpeTree/updateSILVA/")
w_file = open('kegg_abb_to_ncbi_tax.txt', 'a')
with open('genome.txt') as f:
    for line in f:
        tem = line.strip().split(';')[0]
        tem2 = tem.split('\t')[1]
        tem3 = tem2.split(',')
        print(tem3)
        if len(tem3) == 2:
            w_file.write('{0}\t{1}\n'.format(tem3[0].strip(), tem3[1].strip()))
        else:
            w_file.write('{0}\t{1}\n'.format(tem3[0].strip(), tem3[2].strip()))
w_file.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~get all SILVA support orgnism~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os

file_path = '/home/yangfang/PhySpeTree/updateSILVA/database16s/'
all_pre_file = list(filter(lambda f: not f.startswith('.'), os.listdir(file_path)))
f_w = open('/home/yangfang/PhySpeTree/updateSILVA/support_srna_organism.txt', 'a')
for i in all_pre_file:
    f_w.write("{0}\n".format(i.strip().split('.')[0]))
f_w.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~deal with NCBI tax to latin name~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

f_write = open('/home/yangfang/PhySpeTree/updateSILVA/id_to_latin_name.txt', 'a')
tem_id = []
with open('/home/yangfang/PhySpeTree/updateSILVA/taxmap_embl_ssu_ref_nr99_132.txt') as f:
    for line in f:
        tem = line.strip().split('\t')
        silva_id = tem[0] + '.' + tem[1] + '.' + tem[2]
        if tem[5] not in tem_id:
            f_write.write("{0}\t{1}\n".format(tem[5],tem[4]))
            tem_id.append(tem[5])
f_write.close()

# ~~~~~~~~~~~~~~~~~~~map silva id to ncbi id~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
f_write = open('/home/yangfang/PhySpeTree/updateSILVA/map_silva_to_ncbi.txt', 'a')

with open('/home/yangfang/PhySpeTree/updateSILVA/taxmap_embl_ssu_ref_nr99_132.txt') as f:
    for line in f:
        tem = line.strip().split('\t')
        silva_id = tem[0] + '.' + tem[1] + '.' + tem[2]
        f_write.write("{0}\t{1}\n".format(silva_id, tem[5]))

f_write.close()

# ~~~~~~~~~~~~~~~~~~~map silva id to ncbi id~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
f_write = open('/home/yangfang/PhySpeTree/updateSILVA/silva.txt', 'a')
tem_id = []
with open('/home/yangfang/PhySpeTree/updateSILVA/taxmap_embl_ssu_ref_nr99_132.txt') as f:
    for line in f:
        tem = line.strip().split('\t')
        silva_id = tem[0] + '.' + tem[1] + '.' + tem[2]
        if tem[5] not in tem_id:
            f_write.write("{0}\t{1}\t{2}\t{3}\n".format(silva_id, tem[5], tem[4], tem[3]))
            tem_id.append(tem[5])
f_write.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os

file_path = '/home/yangfang/PhySpeTree/updateSILVA/database16s/'
all_pre_file = list(filter(lambda f: not f.startswith('.'), os.listdir(file_path)))
for i in all_pre_file:
    new_name = i.strip()
    os.rename('/home/yangfang/PhySpeTree/updateSILVA/database16s/' + i,
              '/home/yangfang/PhySpeTree/updateSILVA/database16s/' + new_name)



f_write = open('/home/yangfang/PhySpeTree/updateSILVA/silva2.txt', 'a')
with open('/home/yangfang/PhySpeTree/updateSILVA/silva.txt') as f:
    for line in f:
        tem = line.strip().split('\t')
        f_write.write("{0}\t{1}\t{2}\n".format(tem[1], tem[2], tem[3]))

f_write.close()
