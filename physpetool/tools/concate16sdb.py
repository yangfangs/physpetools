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

connect = ftplib.FTP("173.255.208.244")
connect.login('anonymous')
connect.cwd('/pub/database16s/')
os.chdir('/home/yangfang/')
downloadfilname = "999421.fasta"
f = open(downloadfilname, 'wb')
ftpfilename = "999421.fasta"
remoteFileName = 'RETR ' + os.path.basename(ftpfilename)
connect.retrbinary(remoteFileName, f.write, 1024)
f.close()


connect.quit()
