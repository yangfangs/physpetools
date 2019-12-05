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
Combine tree module: use this module can combine more tree to a consensus tree.

"""
import os
import subprocess
from physpetool.softwares.path import getlocalpath


def docontree(input, output, rule):
    """
Combine tree
    :param input: input files
    :param output: output directory
    """
    # get raxml path
    raxmlpath = getlocalpath()
    # run

    # prepare a dir store result
    if not os.path.exists(output):
        os.mkdir(output)
    consensuseCmd = raxmlpath + "/raxmlHPC-PTHREADS-AVX2 " + " -J " + rule + " -m GTRCAT -z " + input + " -w " + output + " -n T1"
    subprocess.call(consensuseCmd, shell=True)

def do_astral(input,output):
    astralpath = getlocalpath()
    if not os.path.exists(output):
        os.mkdir(output)
    out_name = "combine.tree"
    consensuseCmd =  "java -jar " + astralpath + "/astral.5.6.3.jar" + " -i " + input+" -o " + output +"/"+ out_name
    subprocess.call(consensuseCmd, shell=True)

def do_supertree(input, output):
    supertreepath = getlocalpath()
    if not os.path.exists(output):
        os.mkdir(output)
    out_name = "spr_supertree.tree"
    consensuseCmd = supertreepath + "/spr_supertree" + " < " + input+" > " + output +"/"+ out_name
    subprocess.call(consensuseCmd, shell=True)