# ########################## Copyrights and License #############################
#                                                                               #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                              #
#                                                                               #
# This file is part of PhySpeTree.                                              #
# https://xiaofeiyangyang.github.io/physpetools/                                #
#                                                                               #
# PhySpeTree is free software: you can redistribute it and/or modify it under   #
# the terms of the GNU Lesser General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)     #
# any later version.                                                            #
#                                                                               #
# PhySpeTree is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS     #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  #
# details.                                                                      #
#                                                                               #
# You should have received a copy of the GNU Lesser General Public License      #
# along with PhySpeTree. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                               #
# ###############################################################################

"""
Connect 16s SSU rRNA database.

"""


import ftplib
import os

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
