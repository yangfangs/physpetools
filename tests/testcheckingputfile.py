from physpetool.utils.checkinputfile import checkSilvaOrganism

filepath = open("/home/yangfang/physpetools/testdata/speciesname.txt")

all = checkSilvaOrganism(filepath)
print (all)