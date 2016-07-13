import ftplib
import os
import urllib2

connect = ftplib.FTP("bioinfor.scu.edu.cn")
connect.login('anonymous')
connect.cwd('/pub')
connect.dir()
os.chdir('/home/yangfang/physpetools/testdata')
downloadfilname = "fwefwef.txt"
f = open(downloadfilname, 'wb')
ftpfilename = "test.txt"
remoteFileName = 'RETR ' + os.path.basename(ftpfilename)
connect.retrbinary(remoteFileName, f.write, 1024)
f.close()


connect.quit()
